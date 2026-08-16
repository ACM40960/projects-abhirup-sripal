from collections import Counter
from itertools import combinations
import difflib

import numpy as np
import pandas as pd

FEATURE_COLUMNS = [
    "home_elo",
    "away_elo",
    "home_form_goals_for",
    "home_form_goals_against",
    "away_form_goals_for",
    "away_form_goals_against",
    "match_weight",
    "is_neutral",
]

CLASS_LABELS = np.array([0, 1, 2])
CLASS_NAMES = {
    0: "Away Win",
    1: "Draw",
    2: "Home Win",
}


def align_probability_columns(model, probabilities, labels=CLASS_LABELS):
    probabilities = np.asarray(probabilities, dtype=float)
    aligned = np.zeros((len(probabilities), len(labels)), dtype=float)

    for source_index, class_label in enumerate(model.classes_):
        destination = np.where(labels == int(class_label))[0]
        if len(destination) != 1:
            raise ValueError(f"Unexpected model class label: {class_label}")
        aligned[:, destination[0]] = probabilities[:, source_index]

    if not np.allclose(aligned.sum(axis=1), 1.0, atol=1e-6):
        raise ValueError("Predicted probabilities do not sum to one.")

    return aligned


def multiclass_brier_score(y_true, probabilities, labels=CLASS_LABELS):
    y_array = np.asarray(y_true, dtype=int)
    one_hot = np.column_stack([
        (y_array == label).astype(float)
        for label in labels
    ])

    return float(
        np.mean(
            np.sum(
                (np.asarray(probabilities, dtype=float) - one_hot) ** 2,
                axis=1,
            )
        )
    )


class MatchPredictor:
    """Team-specific prediction wrapper around the frozen probability model."""

    def __init__(self, model, team_state, feature_columns=None):
        self.model = model
        self.feature_columns = list(feature_columns or FEATURE_COLUMNS)
        self.team_state = team_state.copy()

        if self.team_state["team"].duplicated().any():
            raise ValueError("Team-state snapshot contains duplicate team names.")

        required = {
            "team",
            "current_elo",
            "current_form_goals_for",
            "current_form_goals_against",
        }
        missing = sorted(required - set(self.team_state.columns))
        if missing:
            raise ValueError(f"Team-state snapshot is missing columns: {missing}")

        self.team_state_lookup = self.team_state.set_index("team")
        self.available_teams = set(self.team_state_lookup.index)
        self._probability_cache = {}

    @property
    def cache_size(self):
        return len(self._probability_cache)

    def precompute_neutral_pairs(self, teams, tournament_weight=1.0):
        """Vectorise neutral-pair probability calculation for tournament runs.

        This produces the same symmetrised probabilities as repeated calls to
        ``get_match_probabilities`` but avoids thousands of tiny sklearn
        ``predict_proba`` calls inside Monte Carlo loops.
        """
        teams = list(teams)
        for team in teams:
            self.validate_team_name(team)

        pair_specs = []
        feature_rows = []

        for left_index, team_a in enumerate(teams):
            for team_b in teams[left_index + 1:]:
                key_ab = (team_a, team_b, float(tournament_weight), True)
                key_ba = (team_b, team_a, float(tournament_weight), True)
                if key_ab in self._probability_cache and key_ba in self._probability_cache:
                    continue

                row_ab = self.build_match_features(
                    team_a, team_b, tournament_weight=tournament_weight, neutral=True
                )
                row_ba = self.build_match_features(
                    team_b, team_a, tournament_weight=tournament_weight, neutral=True
                )
                pair_specs.append((team_a, team_b, key_ab, key_ba))
                feature_rows.extend([row_ab.iloc[0].to_dict(), row_ba.iloc[0].to_dict()])

        if not pair_specs:
            return

        feature_frame = pd.DataFrame(feature_rows, columns=self.feature_columns)
        raw = self.model.predict_proba(feature_frame)
        aligned = align_probability_columns(self.model, raw, CLASS_LABELS)

        for pair_index, (team_a, team_b, key_ab, key_ba) in enumerate(pair_specs):
            direct = aligned[2 * pair_index]
            reverse = aligned[2 * pair_index + 1]

            home_win = (float(direct[2]) + float(reverse[0])) / 2.0
            draw = (float(direct[1]) + float(reverse[1])) / 2.0
            away_win = (float(direct[0]) + float(reverse[2])) / 2.0
            total = home_win + draw + away_win
            if total <= 0:
                raise ValueError("Model returned an invalid probability vector.")

            home_win /= total
            draw /= total
            away_win /= total

            self._probability_cache[key_ab] = (home_win, draw, away_win)
            self._probability_cache[key_ba] = (away_win, draw, home_win)

    def validate_team_name(self, team):
        if team in self.available_teams:
            return

        suggestions = difflib.get_close_matches(
            str(team),
            sorted(self.available_teams),
            n=5,
            cutoff=0.5,
        )
        suffix = f" Similar names: {', '.join(suggestions)}." if suggestions else ""
        raise KeyError(
            f"Team '{team}' is not available in the current state snapshot."
            + suffix
        )

    def build_match_features(
        self,
        home_team,
        away_team,
        tournament_weight=1.0,
        neutral=True,
    ):
        self.validate_team_name(home_team)
        self.validate_team_name(away_team)

        if home_team == away_team:
            raise ValueError("A team cannot play itself.")

        home = self.team_state_lookup.loc[home_team]
        away = self.team_state_lookup.loc[away_team]

        return pd.DataFrame([{
            "home_elo": float(home["current_elo"]),
            "away_elo": float(away["current_elo"]),
            "home_form_goals_for": float(home["current_form_goals_for"]),
            "home_form_goals_against": float(home["current_form_goals_against"]),
            "away_form_goals_for": float(away["current_form_goals_for"]),
            "away_form_goals_against": float(away["current_form_goals_against"]),
            "match_weight": float(tournament_weight),
            "is_neutral": int(bool(neutral)),
        }], columns=self.feature_columns)

    def _ordered_probability_vector(
        self,
        home_team,
        away_team,
        tournament_weight,
        neutral,
    ):
        match_features = self.build_match_features(
            home_team,
            away_team,
            tournament_weight=tournament_weight,
            neutral=neutral,
        )
        raw = self.model.predict_proba(match_features)
        return align_probability_columns(
            self.model,
            raw,
            CLASS_LABELS,
        )[0]

    def get_match_probabilities(
        self,
        home_team,
        away_team,
        tournament_weight=1.0,
        neutral=True,
    ):
        key = (
            home_team,
            away_team,
            float(tournament_weight),
            bool(neutral),
        )

        if key not in self._probability_cache:
            direct = self._ordered_probability_vector(
                home_team,
                away_team,
                tournament_weight,
                neutral,
            )

            away_win = float(direct[0])
            draw = float(direct[1])
            home_win = float(direct[2])

            if neutral:
                reverse = self._ordered_probability_vector(
                    away_team,
                    home_team,
                    tournament_weight,
                    neutral,
                )

                home_win = (home_win + float(reverse[0])) / 2.0
                draw = (draw + float(reverse[1])) / 2.0
                away_win = (away_win + float(reverse[2])) / 2.0

            total = home_win + draw + away_win
            if total <= 0:
                raise ValueError("Model returned an invalid probability vector.")

            self._probability_cache[key] = (
                home_win / total,
                draw / total,
                away_win / total,
            )

        home_win, draw, away_win = self._probability_cache[key]

        return {
            "home_team": home_team,
            "away_team": away_team,
            "home_win": home_win,
            "draw": draw,
            "away_win": away_win,
        }


def build_seeded_groups(
    teams,
    predictor,
    group_count=12,
    group_size=4,
):
    teams = list(teams)
    expected_teams = group_count * group_size

    if len(teams) != expected_teams:
        raise ValueError(
            f"Expected {expected_teams} teams for "
            f"{group_count} groups of {group_size}; received {len(teams)}."
        )
    if len(set(teams)) != len(teams):
        raise ValueError("Tournament team list contains duplicates.")

    for team in teams:
        predictor.validate_team_name(team)

    ranked = sorted(
        teams,
        key=lambda team: float(
            predictor.team_state_lookup.loc[team, "current_elo"]
        ),
        reverse=True,
    )

    pots = [
        ranked[index * group_count:(index + 1) * group_count]
        for index in range(group_size)
    ]

    groups = {
        f"Group {chr(65 + index)}": []
        for index in range(group_count)
    }
    group_names = list(groups)

    for pot_number, pot in enumerate(pots):
        order = (
            group_names
            if pot_number % 2 == 0
            else list(reversed(group_names))
        )
        for group_name, team in zip(order, pot):
            groups[group_name].append(team)

    return groups


def _sample_regulation_outcome(predictor, home_team, away_team, rng):
    probabilities = predictor.get_match_probabilities(
        home_team,
        away_team,
        tournament_weight=1.0,
        neutral=True,
    )

    return rng.choice(
        ["home", "draw", "away"],
        p=[
            probabilities["home_win"],
            probabilities["draw"],
            probabilities["away_win"],
        ],
    )


def simulate_group(predictor, group_name, teams, rng):
    points = {team: 0 for team in teams}

    for home_team, away_team in combinations(teams, 2):
        outcome = _sample_regulation_outcome(
            predictor,
            home_team,
            away_team,
            rng,
        )

        if outcome == "home":
            points[home_team] += 3
        elif outcome == "away":
            points[away_team] += 3
        else:
            points[home_team] += 1
            points[away_team] += 1

    standings = pd.DataFrame([
        {
            "group": group_name,
            "team": team,
            "points": points[team],
            "elo_tiebreak": float(
                predictor.team_state_lookup.loc[team, "current_elo"]
            ),
        }
        for team in teams
    ])

    standings = (
        standings
        .sort_values(
            ["points", "elo_tiebreak"],
            ascending=[False, False],
        )
        .reset_index(drop=True)
    )
    standings["group_position"] = np.arange(
        1,
        len(standings) + 1,
    )

    return standings


def simulate_knockout_match(predictor, team_a, team_b, rng):
    probabilities = predictor.get_match_probabilities(
        team_a,
        team_b,
        tournament_weight=1.0,
        neutral=True,
    )

    regulation = rng.choice(
        ["team_a", "draw", "team_b"],
        p=[
            probabilities["home_win"],
            probabilities["draw"],
            probabilities["away_win"],
        ],
    )

    if regulation == "team_a":
        return team_a
    if regulation == "team_b":
        return team_b

    non_draw_total = (
        probabilities["home_win"]
        + probabilities["away_win"]
    )

    team_a_advance = (
        0.5
        if non_draw_total <= 0
        else probabilities["home_win"] / non_draw_total
    )

    return rng.choice(
        [team_a, team_b],
        p=[team_a_advance, 1.0 - team_a_advance],
    )


def build_round_of_32_pairs(qualifiers):
    remaining = (
        qualifiers
        .sort_values(
            ["group_position", "points", "elo_tiebreak"],
            ascending=[True, False, False],
        )
        .to_dict("records")
    )

    pairs = []

    while remaining:
        high_seed = remaining.pop(0)

        opponent_index = None
        for candidate_index in range(len(remaining) - 1, -1, -1):
            if (
                remaining[candidate_index]["group"]
                != high_seed["group"]
            ):
                opponent_index = candidate_index
                break

        if opponent_index is None:
            opponent_index = len(remaining) - 1

        low_seed = remaining.pop(opponent_index)
        pairs.append((high_seed["team"], low_seed["team"]))

    return pairs


def run_single_tournament(predictor, groups, rng):
    # Use plain Python records inside the Monte Carlo loop. Creating pandas
    # DataFrames for every one of 12 groups in every simulation dominated the
    # runtime while adding no modelling value.
    all_group_records = []

    for group_name, teams in groups.items():
        points = {team: 0 for team in teams}

        for home_team, away_team in combinations(teams, 2):
            outcome = _sample_regulation_outcome(
                predictor,
                home_team,
                away_team,
                rng,
            )

            if outcome == "home":
                points[home_team] += 3
            elif outcome == "away":
                points[away_team] += 3
            else:
                points[home_team] += 1
                points[away_team] += 1

        ranked_teams = sorted(
            teams,
            key=lambda team: (
                points[team],
                float(predictor.team_state_lookup.loc[team, "current_elo"]),
            ),
            reverse=True,
        )

        for position, team in enumerate(ranked_teams, start=1):
            all_group_records.append({
                "group": group_name,
                "team": team,
                "points": points[team],
                "elo_tiebreak": float(
                    predictor.team_state_lookup.loc[team, "current_elo"]
                ),
                "group_position": position,
            })

    automatic_qualifiers = [
        record for record in all_group_records
        if record["group_position"] <= 2
    ]

    third_place = sorted(
        [
            record for record in all_group_records
            if record["group_position"] == 3
        ],
        key=lambda record: (
            record["points"],
            record["elo_tiebreak"],
        ),
        reverse=True,
    )[:8]

    qualifiers = automatic_qualifiers + third_place
    if len(qualifiers) != 32:
        raise ValueError(
            f"Expected 32 knockout qualifiers, found {len(qualifiers)}."
        )

    stage_reached = {
        team: "Group"
        for teams in groups.values()
        for team in teams
    }

    for record in qualifiers:
        stage_reached[record["team"]] = "R32"

    remaining = sorted(
        qualifiers,
        key=lambda record: (
            record["group_position"],
            -record["points"],
            -record["elo_tiebreak"],
        ),
    )

    current_pairs = []
    while remaining:
        high_seed = remaining.pop(0)
        opponent_index = None

        for candidate_index in range(len(remaining) - 1, -1, -1):
            if remaining[candidate_index]["group"] != high_seed["group"]:
                opponent_index = candidate_index
                break

        if opponent_index is None:
            opponent_index = len(remaining) - 1

        low_seed = remaining.pop(opponent_index)
        current_pairs.append((high_seed["team"], low_seed["team"]))

    round_names = ["R32", "R16", "QF", "SF", "Final"]
    next_stage = {
        "R32": "R16",
        "R16": "QF",
        "QF": "SF",
        "SF": "Final",
        "Final": "Champion",
    }

    for round_name in round_names:
        winners = []

        for team_a, team_b in current_pairs:
            winner = simulate_knockout_match(
                predictor,
                team_a,
                team_b,
                rng,
            )
            winners.append(winner)
            stage_reached[winner] = next_stage[round_name]

        if len(winners) == 1:
            champion = winners[0]
            break

        current_pairs = [
            (winners[index], winners[index + 1])
            for index in range(0, len(winners), 2)
        ]

    return champion, stage_reached

def run_monte_carlo_tournament(
    predictor,
    groups,
    iterations=2000,
    seed=42,
):
    if iterations <= 0:
        raise ValueError("iterations must be positive.")

    all_teams = [
        team
        for teams in groups.values()
        for team in teams
    ]

    if len(all_teams) != 48 or len(set(all_teams)) != 48:
        raise ValueError(
            "This tournament configuration expects 48 unique teams."
        )

    rng = np.random.default_rng(seed)
    stage_counts = {
        team: Counter()
        for team in all_teams
    }

    for _ in range(iterations):
        champion, stage_reached = run_single_tournament(
            predictor,
            groups,
            rng,
        )

        for team, stage in stage_reached.items():
            stage_counts[team][stage] += 1

    ordered_stages = [
        "R32",
        "R16",
        "QF",
        "SF",
        "Final",
        "Champion",
    ]

    rows = []

    for team in all_teams:
        counts = stage_counts[team]

        champion_count = counts["Champion"]
        final_count = counts["Final"] + champion_count
        sf_count = counts["SF"] + final_count
        qf_count = counts["QF"] + sf_count
        r16_count = counts["R16"] + qf_count
        r32_count = counts["R32"] + r16_count

        cumulative = {
            "R32": r32_count,
            "R16": r16_count,
            "QF": qf_count,
            "SF": sf_count,
            "Final": final_count,
            "Champion": champion_count,
        }

        rows.append({
            "team": team,
            "current_elo": float(
                predictor.team_state_lookup.loc[
                    team,
                    "current_elo",
                ]
            ),
            **{
                f"{stage.lower()}_probability":
                    cumulative[stage] / iterations
                for stage in ordered_stages
            },
        })

    return (
        pd.DataFrame(rows)
        .sort_values(
            ["champion_probability", "final_probability"],
            ascending=False,
        )
        .reset_index(drop=True)
    )
