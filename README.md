# oil2corn-transmission-ethanol
Oil–Corn Futures Transmission: The Role of Ethanol Economics

(1) Overview
This project analyzes the relationship between crude oil and corn futures,
with a focus on whether ethanol-related energy dynamics act as a transmission mechanism.

Using 20+ years of data, the analysis evaluates:
- baseline correlations
- oil shock effects
- volatility regimes
- energy linkage conditions (oil–gasoline correlation proxy)

(2) Key Findings
- Oil–corn correlation is weak in baseline conditions (~0.19)
- Oil shocks increase corn volatility but do not predict direction
- Correlation strengthens in high-volatility environments
- When oil–gasoline linkage is strong, oil–corn correlation increases (~0.14 → ~0.23)

Conclusion:
Cross-commodity transmission exists but is conditional and not sufficient
for standalone trading strategies.

(3) Methodology
- Data: Yahoo Finance (CL=F, ZC=F, RB=F)
- Period: 2000–2026
- Log returns used for analysis
- Techniques:
  - correlation analysis
  - rolling correlations
  - regime segmentation
  - conditional comparisons

(4) Repository Structure
- report/: final write-up
- notebooks/: data processing and analysis
- outputs/: charts used in report
- data_clean/: processed dataset

(5) How to Reproduce
Run notebooks in order:

1. phase2_data.ipynb
2. phase3_analysis.ipynb
