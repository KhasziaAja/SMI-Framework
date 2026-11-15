# SMI Framework: Empirical Benchmarks and Open Issues Master (BENCHMARK_AND_ISSUES) - v1.1

[English](./BENCHMARK_AND_ISSUES.md) | [日本語](./BENCHMARK_AND_ISSUES.ja.md)

> **"Uncalibrated parameters and empirical gaps are not structural flaws; they represent the open frontier where researchers and data scientists worldwide converge to determine optimal coefficients."**

## 1. Scientific Falsifiability & Model Rejection Protocol

To maintain scientific integrity and prevent degeneration into subjective moralizing, the SMI Framework predefines explicit boundary conditions under which the core hypothesis must be rejected.

### 1.1 Operational Runtime Preconditions

This falsification protocol operates exclusively within environments satisfying three structural preconditions characteristic of modern urban capitalist social systems (defined in `SPECIFICATION_LITE.md` Section 1):

1. **Monetized Market Economy:** The vast majority of baseline survival, housing, and reproductive costs are procured through competitive markets and settled in fiat currency (excluding pure subsistence barter economies or unpriced command ration systems).

2. **Individual Autonomy & Free Will:** Individuals maintain unrestricted legal, statutory, and cultural rights over marriage, contraception, and personal lifestyle (excluding forced reproduction under institutional coercion or religious dogma).

3. **Offspring as Net Economic Liabilities (**$P_{net} < 1.0$**):** Mandatory education and child labor bans ensure dependent children represent continuous unidirectional consumption overhead for 18–22 years.

### 1.2 Model Rejection Criteria (Null Hypotheses)

Under the operational preconditions above, the core architecture of the SMI Framework shall be considered falsified and subject to immediate discarding or fundamental revision upon empirical demonstration of any of the following:

1. **Unresponsiveness to Long-Term Sovereign De-Compression (**$SMI \ge 2.00$**):**
   If a sovereign state or regional administrative unit elevates the median real SMI (**Standard Lens**) of young single adults (ages 25–34) to $SMI \ge 2.00$ via direct structural denominator cuts (housing, statutory fiscal drag) and sustains this level for ten consecutive calendar years (two biological clock cycles), yet the Total Fertility Rate (TFR) demonstrates no statistically significant upward inflection ($p < 0.05$) beginning 4 to 6 years post-intervention.

2. **Temporal Inversion of Macro-Causality:**
   If Granger causality tests across peacetime cross-national panel data show that macroeconomic fertility fluctuations statistically precede directional shifts in $SMI$ ($TFR_t \to SMI_{t+k}$), while the hypothesis of $SMI_{t-k} \to TFR_t$ is empirically rejected.

3. **Falsification of the Labor Market Floor Constant (**$\approx 0.45$**):**
   If within the self-supporting labor cohort (**Track A**, strictly excluding public transfer/exempt cohorts in Track B), numerous advanced urban jurisdictions sustain extreme Canary-tier compression ($SMI_{canary} < 0.35$) for over 10 consecutive years without triggering labor abandonment, underground economy migration, or public order degradation, the floor constant hypothesis shall be revised or discarded.

## 2. Standard Benchmark Datasets

To ensure standardized replication and backtesting, the following authoritative statistical registers are designated as reference verification baselines (analogous to the MNIST dataset in machine learning):

### 2.1 Recommended Public Data Sources

* **Japan Historical Benchmark (1970–Present):**

  * **Numerator (**$WCI$**):** Statistics Bureau of Japan *Family Income and Expenditure Survey (FIES: Single & Worker Households)*, National Tax Agency *Statistical Survey of Actual Status for Salary in the Private Sector*.

  * **Denominator (**$C_{surv\_std}$**):** Statistics Bureau *Retail Price Survey* & *Housing and Land Survey* (private market rents), statutory tax/social insurance schedules, MEXT *Survey of Children's Learning Expenses*.

  * **Response Metric (**$TFR$**):** Ministry of Health, Labour and Welfare (MHLW) *Vital Statistics of Japan*.

* **United States Benchmark:**

  * **Numerator & Denominator:** US Census Bureau *Current Population Survey (CPS)*, HUD *Fair Market Rents (FMR)*, Bureau of Labor Statistics (BLS) *Consumer Expenditure Survey (CES)*.

  * **Response Metric:** CDC National Center for Health Statistics (NCHS).

* **Cross-National 4-Country Validation Set (Canary & Floor Verification):**

  * **Target Jurisdictions:** United States (free-market/low-welfare), Sweden (high-tax/universal in-kind welfare), Italy (familialist Southern European regime), and Hungary (aggressive family tax-exemption/subsidy regime).

  * **Verification Scope:** Segregating Track A (self-supporting market workers) from Track B (public transfer/exempt cohorts) to verify that the Canary cohort ($Q25\text{–}Q40$) converges universally onto the $0.44 \sim 0.53$ **Labor Market Floor**, and that breaching $0.60$ precedes median middle-class collapse by **12 to 15 years** (Data Sources: LIS Cross-National Data Center, Eurostat EU-SILC, OECD.Stat).

### 2.2 Econometric Verification Protocols (Eliminating Spurious Correlation)

To eliminate spurious long-term trend matching, all submitted backtests must pass the following three-tier verification protocol:

1. **Level Fit & Peak Lag Identification:** Compute coefficient of determination ($R^2$) and Cross-Correlation Function (CCF) peak lags between observed $TFR_t$ and predicted trajectories processed through the 3–5 year finite impulse response kernel (FIR: $w_3=0.20, w_4=0.65, w_5=0.15$).

2. **Detrended First-Difference Test:** Perform unit root tests (ADF) and evaluate first-difference correlations ($\Delta SMI_{t-4}$ vs. $\Delta TFR_t$) alongside structural break alignment to rule out non-stationary trend artifacts.

3. **Out-of-Sample Forecasting:** Calibrate model parameters strictly on pre-cutoff windows (e.g., pre-1990) and evaluate predictive trajectory accuracy across unseen test horizons (e.g., 1991–present).

### 2.3 Quick Verification & Reproducibility Script

To enable external researchers and quantitative analysts to immediately verify the model's empirical lag dynamics ($t+4$ phase delay and $R^2 \approx 0.85$ trajectory tracking) within their own environments, an official verification script is included in the repository:

* **Script Path:** [`scripts/verify_japan_benchmark.py`](/scripts/verify_japan_benchmark.py)

* **Execution Environment:** Python 3.9+ (requires `numpy`, `pandas`, `scipy`, `matplotlib`) / Google Colab compatible.

* **Verification Scope:** Automated cross-correlation function (CCF) execution and phase-shifted plotting utilizing unadjusted time-series tables from the Japanese Statistics Bureau (*FIES*) and MHLW (*Vital Statistics of Japan*).

## 3. Academic Open Issue Master List (Layer 1 Public Frontier)

The following priority research vectors are triaged by academic domain to facilitate targeted pull requests and independent peer investigation on the public Layer 1 protocol:

### ■ Category A: Econometric & Data Pipelines

* \[ \] **Issue #01: Automated Data Extraction Pipeline (ETL) for** $WCI$ **and Standard Denominator (**$C_{surv\_std}$**)**

  * **Current State:** The theoretical formula $SMI = \frac{WCI}{C_{surv\_std}}$ is established, but accounting taxonomies differ across national registers (SNA, FIES, CPS, Eurostat, OECD).

  * **Task:** Develop reproducible Python/R packages to programmatically ingest raw government tables (excluding headline CPI deflators), extract median single disposable income ($WCI$), and map baseline survival overhead into `SMILayer1InputSchema_v1_1` JSON format.

* \[ \] **Issue #02: Calibration of Positional Status Cost Function (**$\theta \cdot R_{rel}$**)**

  * **Current State:** The relative cost term capturing local educational competition and social conformity pressure ($\theta \in [0.0, 1.0]$) must be derived systematically from observable economic variables rather than ad-hoc fitting.

  * **Task:** Formalize panel regressions linking local higher-education enrollment ratios, median private tutoring expenditures, and spatial Gini coefficients to establish deterministic values for $\theta$ across cultural regimes.

* \[ \] **Issue #03: Household Time-Depletion Discount Parameter (**$\lambda \approx 0.35$**) for Dual-Earner Cohorts**

  * **Current State:** Combining dual incomes without accounting for non-market labor depletion overstates real household margin (the "1.5-Earner Trap").

  * **Task:** Utilize time-use microdata (e.g., American Time Use Survey, Japanese Survey on Time Use) and commercial childcare/outsourcing expenditure indices to estimate the decay elasticity parameter $\lambda$ in $WCI_{eff}$.

* \[ \] **Issue #13: Automated Extraction & Separation Pipeline for Canary Cohorts (**$Q25\text{–}Q40$**) and Track A / Track B Regimes**

  * **Current State:** Extending the 4-country empirical findings (the $\approx 0.45$ Labor Market Floor and 12–15 year early-warning lead time) across all OECD economies requires an automated microdata algorithm separating self-supporting market workers (Track A) from public-transfer/exempt cohorts (Track B).

  * **Task:** Utilizing LIS (Luxembourg Income Study) and national microdata panels, isolate households receiving full housing vouchers or statutory tax/insurance exemptions into Track B, and compute Track A floor convergence ($0.44 \sim 0.53$) alongside lead-time horizons ($\Delta t_{lead}$) prior to median middle-class compression.

### ■ Category B: Evolutionary Biology & Time-Series Dynamics

* \[ \] **Issue #04: Cross-Correlation Function (CCF) Mapping of Urban Size vs. Distributed Lag Vectors**

  * **Current State:** National macro panels exhibit a sharp correlation peak at $t+4$ years, but variance in lag weights ($w_3, w_4, w_5$) between high-density megacities and regional municipalities requires quantification.

  * **Task:** Estimate CCF and Autoregressive Distributed Lag (ARDL) models across prefectural/state-level panels to measure how housing cost rigidity shifts biological response lags.

* \[ \] **Issue #05: Meta-Analysis of Charnov Invariants vs. Mammalian Reproductive Gestation Delays**

  * **Current State:** Evolutionary life-history theory indicates that recovery-to-parturition latency scales with $\approx 5\%$ of adult life expectancy ($\approx 4$ years in humans) across K-selected large mammals.

  * **Task:** Aggregate empirical life-history datasets across $\ge 12$ long-lived mammalian/primate species to cross-validate physiological recovery scaling laws against urban human demographic panels.

* \[ \] **Issue #06: Empirical Parameter Calibration for the 4PL Sigmoid Transfer Function (**$k, SMI_0$**)**

  * **Current State:** While baseline parameters ($SMI_0 \approx 1.05, k \approx 4.0$) capture aggregate saturation, institutional differences (e.g., universal in-kind childcare) may alter phase-transition steepness $k$.

  * **Task:** Execute Non-Linear Least Squares (NLS) fitting across Nordic, Anglo-Saxon, and East Asian longitudinal panels to calibrate regime-specific steepness and inflection parameters.

* \[ \] **Issue #12: Coordinated Physiological Transient Responses under Chronic Low-SMI States (HPG-Axis Inhibition vs. HPA-Axis Hyper-Activation)**

  * **Current State:** Existential survival compression under chronic low-SMI states simultaneously drives multiple adaptive biological systemic errors: autonomic reproductive shutdown (HPG-axis suppression), defensive visceral fat hoarding (inverse BMI escalation), and slow-wave sleep architecture collapse (HPA-axis hyper-activation).

  * **Task:** Cross-reference longitudinal regional SMI series with public health surveillance panels (e.g., MHLW National Health and Nutrition Survey, CDC NHANES) to quantify inverse BMI dynamics, and aggregate clinical cortisol, gonadotropin (GnRH/free testosterone), and HRV biomarkers across low-SMI cohorts.

### ■ Category C: Institutional Engineering & Implementation

* \[ \] **Issue #10: Actuarial Neutrality of Life-Cycle Stage Taxation (Early Exemption / Late Clawback)**

  * **Current State:** Exempting young cohorts (ages 20–35) from income taxes and social security withholdings to secure $SMI \ge 1.40$ requires actuarially balanced clawback mechanisms during peak earning years (ages 50–64) once child-rearing overheads conclude.

  * **Task:** Construct Overlapping Generations (OLG) dynamic macroeconomic simulations to verify long-term fiscal solvency and demographic replacement recovery.

* \[ \] **Issue #11: Cross-Jurisdictional Tax Compatibility of Corporate-Leased Employee Housing (B2B Denomination Compression)**

  * **Current State:** Substituting taxable cash wages with corporate-leased in-kind housing compresses both employee tax/social insurance wedges and residential fixed overhead simultaneously.

  * **Task:** Compile a comparative legal and tax matrix across Japanese fringe-benefit rulings, US IRC Section 119 / LIHTC / Employer-Assisted Housing, and European housing-allowance tax regimes.

## 4. Quarantined Layer 2 Core Research Vectors

Advanced sovereign security and spatial governance research tasks—including localized spatial density ($D_{local}$), normative cultural distance ($H_{dist}$), non-linear friction calibration ($\text{Toxicity}$), spatial phase separation (Phase 1–3 / Point of No Return), and 20-year generational defense trajectories (**Issue #C01–#C04**)—are strictly quarantined from this public repository.

Qualified research institutions and defense/policy analysts may request vetted access via the portal specified in [`README.md`](/README.md).

## 5. Verification Protocol Requirements (Anti-Overfitting Rules)

To ensure contributions represent generalizable physical laws rather than post-hoc curve fitting, all submitted pull requests and parameter calibrations must satisfy the following rules:

1. **No Ad-Hoc Overfitting:** Arbitrary dummy variables or country-specific fudge factors tuned to single-era noise will be rejected. All modifications must demonstrate superior out-of-sample predictive accuracy across multi-national panels.

2. **Strict Exclusion of Headline CPI:** Code submissions applying aggregate Consumer Price Index (Headline CPI) deflators to the survival denominator ($C_{surv\_std}$) will be rejected automatically.

3. **Mandatory Dual-Track Separation:** Cross-national empirical submissions must segregate self-supporting labor cohorts (Track A) from public transfer/exempt cohorts (Track B) in accordance with `SMILayer1InputSchema_v1_1`.
