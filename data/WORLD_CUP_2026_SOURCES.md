# 2026 World Cup result sources

`world_cup_2026_actual_results.csv` is kept separate from the historical modelling file so tournament outcomes cannot enter the frozen Commit 11 pipeline.

## Structured ground truth

The 72 group results and 32 knockout results are adapted from the WC2026-Agents dataset:

Ding, Jiacheng; Guo, Cong; Xu, Jason (2026), *FIFA World Cup 2026 as a Contamination-Free Benchmark for LLM Forecasting Agents: Four Models, a Bookmaker, and 104 Matches*, arXiv:2607.17765.

Repository: `graphuofm/FIFA2026LLM`

Relevant source tables:

- `data/metadata/results.csv`
- `data/metadata/schedule.csv`
- `data/metadata/results_knockout.csv`
- `data/metadata/schedule_knockout.csv`

The repository states that its `data/` directory is released under CC BY 4.0.

## FIFA cross-check

FIFA's official 2026 World Cup fixtures/results pages and final tournament standings were used as the authoritative cross-check for the tournament finish and key knockout outcomes.

One metadata discrepancy is recorded explicitly: the WC2026-Agents knockout table labels the Spain–Argentina final as `decided_by=regulation`, while FIFA reports Spain's 1-0 winner in extra time. This project therefore records the final as `decided_by=extra_time`; the three-way result remains a Spain win in either representation.

No World Cup score is written back into `data/results.csv`.
