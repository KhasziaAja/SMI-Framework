# SMI Framework: Empirical Benchmarks and Open Issues Master (BENCHMARK_AND_ISSUES) - v1.0

[English](./BENCHMARK_AND_ISSUES.md) | [日本語](./BENCHMARK_AND_ISSUES.ja.md)

> **"Uncalibrated parameters and empirical gaps are not structural flaws; they represent the open frontier where researchers and data scientists worldwide converge to determine optimal coefficients."**

---

## 1. Scientific Falsifiability & Model Rejection Protocol

To maintain scientific integrity and prevent degeneration into subjective moralizing, the SMI Framework predefines explicit boundary conditions under which the core hypothesis must be rejected.

### 1.1 Operational Runtime Preconditions
This falsification protocol operates exclusively within environments satisfying three structural preconditions characteristic of modern urban capitalist social systems:
1. **Monetized Market Economy:** The vast majority of baseline survival, housing, and reproductive costs are procured through competitive markets and settled in fiat currency (excluding pure subsistence barter economies or unpriced command ration systems).
2. **Individual Autonomy & Free Will:** Individuals maintain unrestricted legal, statutory, and cultural rights over marriage, contraception, and personal lifestyle (excluding forced reproduction under institutional coercion or religious dogma).
3. **Offspring as Net Economic Liabilities ($P_{net} < 1.0$):** Mandatory education and child labor bans ensure dependent children represent continuous unidirectional consumption overhead for 18–22 years.

### 1.2 Model Rejection Criteria (Null Hypotheses)

Under the operational preconditions above, the core architecture of the SMI Framework shall be considered falsified and subject to immediate discarding or fundamental revision upon empirical demonstration of any of the following:

1. **Unresponsiveness to Long-Term Sovereign De-Compression ($SMI \ge 2.00$):**  
   If a sovereign state or regional administrative unit elevates the median real SMI of young single adults (ages 25–34) to $SMI \ge 2.00$ (Emergency Impulse Regime) via direct structural denominator cuts (housing, statutory fiscal drag) and sustains this level for ten consecutive calendar years, yet the Total Fertility Rate (TFR) demonstrates no statistically significant upward inflection ($p < 0.05$) beginning 4 to 6 years post-intervention.
2. **Temporal Inversion of Macro-Causality:**  
   If Granger causality tests across cross-national panel data show that macroeconomic fertility fluctuations statistically precede directional shifts in $SMI$ ($TFR_t \to SMI_{t+k}$), while the hypothesis of $SMI_{t-k} \to TFR_t$ is empirically rejected.
3. **Persistent Autonomic Shutdown in Zero-Denominator Environments:**  
   If an experimental cohort provided with unconditional baseline zero-denominator guarantees (100% state-subsidized housing, fully paid healthcare and education, zero marginal fiscal drag) and adequate disposable cognitive time fails to release autonomic mating inhibition (cessation of chronic HPA-axis hyper-activation), demonstrating continued reproductive avoidance.

---

## 2. Standard Benchmark Datasets

To ensure standardized replication and backtesting, the following authoritative statistical registers are designated as reference verification baselines (analogous to the MNIST dataset in machine learning):

### 2.1 Recommended Public Data Sources

| Target Region | Primary Public Database | Extraction Series | SMI Target Mapping |
| :--- | :--- | :--- | :--- |
| **Japan (JP)** | Statistics Bureau of Japan: *FIES (Single Households)*<br>*Population Census*, *Housing and Land Survey*<br>MHLW: *Vital Statistics of Japan* | Single-earner median disposable income (20s–30s)<br>Private market rent, effective statutory tax/social levies<br>Annual TFR, marriage counts | $WCI$<br>$C_{rent}, C_{tax\_ins}$<br>$TFR_t$ |
| **United States (US)** | US Census Bureau: *Current Population Survey (CPS)*<br>Bureau of Labor Statistics (BLS): *CES*<br>CDC / NCHS: *NVSS (Births)* | Median Usual Weekly Earnings (25–34)<br>Fair Market Rents (HUD FMR), Out-of-pocket Healthcare<br>State-level TFR | $WCI$<br>$C_{rent}, C_{health}$<br>$TFR_t$ |
| **Cross-National (OECD)** | OECD Family Database<br>OECD National Accounts at a Glance<br>World Bank World Development Indicators | Net disposable income by household type<br>Childcare and housing cost indicators<br>Total Fertility Rates (1970–present) | $WCI$<br>$C_{surv\_std}, S_{gov}$<br>$TFR_t$ |

### 2.2 Econometric Verification Protocols

1. **Differencing and Stationarity Verification:**  
   Perform unit root tests (ADF test) on raw series; if non-stationarity is confirmed, transform series into first differences ($\Delta SMI_t, \Delta TFR_t$) to eliminate spurious correlations.
2. **Cross-Correlation Function (CCF) Validation:**  
   Compute cross-correlations between $SMI_{t-k}$ and $TFR_t$ over $k = 0 \dots 10$, verifying that the impulse response function conforms to the distributed lag vector (FIR: $w_3=0.20, w_4=0.65, w_5=0.15$) with a dominant peak at $k = 3 \sim 5$ (primary peak at $4.0$ years).

#### 2.3 Quick Verification & Reproducibility Script
To enable external researchers and quantitative analysts to immediately verify the model's empirical lag dynamics ($t+4$ phase delay and $R^2 \approx 0.85$ trajectory tracking) within their own environments, an official verification script is provided in the repository.

* **Script Path:** [`scripts/verify_japan_benchmark.py`](/scripts/verify_japan_benchmark.py)
* **Execution Environment:** Python 3.9+ (requires `numpy`, `pandas`, `scipy`, `matplotlib`) / Google Colab compatible
* **Verification Scope:** Automated cross-correlation function (CCF) execution and phase-shifted plotting utilizing unadjusted time-series tables from the Japanese Statistics Bureau (*Family Income and Expenditure Survey*) and MHLW (*Vital Statistics of Japan*).

---

## 3. Academic Open Issue Master List (Public Protocol Verification)

The following priority research vectors are triaged by academic domain to facilitate targeted pull requests and independent peer investigation on the public Layer 1 protocol:

### ■ Category A: Econometric & Data Pipelines (For Econometricians & Data Engineers)

* [ ] **Issue #01: Automated Data Extraction Pipeline (ETL) for $WCI$ and Standard Denominator ($C_{surv\_std}$)**  
  * **Current State:** The theoretical formula $SMI = \frac{WCI}{C_{surv\_std}}$ is established, but accounting taxonomies differ across national registers (SNA, FIES, CPS, OECD).  
  * **Task:** Develop reproducible Python/R scripts to programmatically ingest raw government tables, extract median single disposable income ($WCI$), and isolate baseline survival overhead ($C_{base} + C_{semi}$).
* [ ] **Issue #02: Calibration of Positional Status Cost Function ($\theta \cdot R_{rel}$)**  
  * **Current State:** The relative cost term capturing local status competition must be derived systematically from observable economic variables rather than ad-hoc fitting.  
  * **Task:** Formalize the parameter vector linking local higher-education enrollment ratios, median private tutoring expenditures, and spatial Gini coefficients to establish deterministic values for $\theta$ across regional markets.
* [ ] **Issue #03: Household Time-Depletion Discount Parameter ($\lambda$) for Dual-Earner Cohorts**  
  * **Current State:** Combining dual incomes without accounting for non-market labor depletion overstates real household margin (the "1.5-Earner Trap").  
  * **Task:** Utilize time-use microdata (e.g., American Time Use Survey, Japanese Survey on Time Use) and commercial service substitution indices to estimate the elasticity parameter $\lambda$ in $WCI_{eff}$.
* [ ] **Issue #04: Implementation of Modular International Normalization Adapters**  
  * **Current State:** Cross-national institutional variance (Nordic in-kind family vouchers, US private health deductibles, Korean *Jeonse* housing deposits) must map cleanly to the base SMI equation.  
  * **Task:** Codify the public transfer offset ($S_{gov}$) for high-welfare economies and the income quintile clustering engine ($Q_1 \dots Q_5$) for polarized market economies.

### ■ Category B: Evolutionary Biology & Time-Series Dynamics (For Biologists & Statisticians)

* [ ] **Issue #05: Cross-Correlation Function (CCF) Mapping of the 3–5 Year Distributed Lag Vector**  
  * **Current State:** The empirical transmission lag between SMI shocks and demographic fertility requires formal multi-country lag-distribution fitting.  
  * **Task:** Run cross-correlation functions (CCF) and vector autoregression (VAR) on historical 50-year panels across G7 economies to confirm the peak weighting vector ($\mathbf{w} = [w_3, w_4, w_5]$) centering at $t+4$ years.
* [ ] **Issue #06: Meta-Analysis of Charnov Invariants vs. Mammalian Reproductive Gestation Delays**  
  * **Current State:** Evolutionary biology demonstrates that environmental recovery-to-parturition scaling correlates with ~5% of adult life expectancy across large K-strategy mammals.  
  * **Task:** Aggregate empirical life-history datasets across $\ge 12$ long-lived mammalian species, confirming that physiological recovery latency conforms to a universal scaling invariant matching the human ~4-year interval.
* [ ] **Issue #07: Empirical Parameter Calibration for the 4PL Sigmoid Transfer Function**  
  * **Current State:** The 4PL logistic function resolves the high-income demographic paradox via asymptotic saturation, but regional steepness ($k$) requires empirical calibration.  
  * **Task:** Fit historical microdata to calibrate $k \approx 4.00$, inflection threshold $SMI_0 \approx 1.05$, and upper carrying-capacity bounds $TFR_{max} \approx 2.15$ across distinct urbanization levels.
* [ ] **Issue #08: Global Labor Arbitrage Depletion Horizon (Point of Exhaustion Modeling)**  
  * **Current State:** Developing states undergo rapid demographic transitions as urbanization shifts offspring from net economic assets ($P_{net} > 1.0$) to structural cost burdens ($P_{net} < 1.0$).  
  * **Task:** Model TFR trajectories and rural-to-urban migration rates across primary sending nations (e.g., Vietnam, Thailand, India, Latin America) to forecast the terminal date ("Point of Exhaustion") when international surplus labor pools permanently evaporate.
* [ ] **Issue #12: Coordinated Physiological Transient Responses under Chronic Low-SMI States (HPG-Axis Inhibition vs. HPA-Axis Hyper-Activation)**
    * **Context & Problem:** The acute existential threat signal triggered by chronic low-SMI conditions (disposable survival margin exhaustion) simultaneously drives multiple adaptive biological systemic errors: not only the autonomic shutdown of reproductive throughput (precipitous TFR decline), but also defensive metabolic hoarding (elevated BMI / visceral adiposity inverse correlation) and sleep architecture degradation (nocturnal hyper-arousal / slow-wave sleep deprivation). These manifestations likely represent unified evolutionary survival countermeasures rather than isolated lifestyle pathologies.
    * **Objectives & Verification Scope:** 
      1. Cross-national validation of longitudinal SMI trends against public health surveillance panels (e.g., MHLW National Health and Nutrition Survey, CDC NHANES) to map the inverse dynamics between structural margins and population-level BMI trajectories.
      2. Systematic literature meta-analysis and clinical aggregation of biological co-markers—specifically salivary/serum cortisol elevation, gonadotropin suppression (pulsatile GnRH / free testosterone attenuation), and heart rate variability (HRV) vagal withdrawal within chronic low-SMI cohorts.

### ■ Category C: Institutional Engineering & Implementation

* [ ] **Issue #09: Actuarial Neutrality of Life-Cycle Stage Taxation (The 50s Clawback Engine)**  
  * **Current State:** Eradicating the survival denominator for young cohorts (ages 20–34) requires compensatory clawback mechanisms once parental child-rearing obligations dissolve (ages 50–64).  
  * **Task:** Construct dynamic microsimulation models testing revenue neutrality and built-in automatic stabilization under restructured personal income tax and earned income tax credit (EITC) architectures.
* [ ] **Issue #10: Corporate Tax Shield Harmonization for Housing Cost Pre-Tax Deduction**  
  * **Current State:** Substituting gross taxable salaries with corporate-leased employee housing (shifting personal rent into deductible corporate operational expenses) dramatically recovers employee SMI.  
  * **Task:** Review jurisdictional compatibility under US IRC Section 119, French social security exemptions, and German corporate fringe benefit standards to establish universal compliance guidelines.
* [ ] **Issue #11: Mathematical Cap Protocol for Effective-SMI Inversion Anomalies**  
  * **Current State:** Full-coverage welfare mechanisms (where the state absorbs housing, healthcare, and utilities) can produce higher effective SMI scores for non-working recipients than entry-level full-time market labor, distorting systemic incentive structures.  
  * **Task:** Design a dynamic policy algorithm establishing an SMI cap linked to minimum-wage labor margins to preserve structural parity and prevent systemic labor desertion.

---

> **🔒 【Access Protocols for Layer 2 Core Research Issues】**  
> Advanced security research vectors—including localized spatial friction calibrations ($\text{Toxicity}$), spatial clustering metrics ($C_{cluster}$), and 20-year generational phase transition thresholds (Phase 3 Point of No Return)—are strictly quarantined from this public repository.  
> These issues are tracked within private institutional repositories (SMI-Framework-Core) to protect sovereign stability. Qualified research organs and institutional defense analysts may request vetted access via the procedure outlined in repository security guidelines.

---

## 4. Verification Protocol Requirements (Anti-Overfitting Rules)

To ensure contributions represent generalizable scientific laws rather than post-hoc curve fitting, all submitted pull requests and parameter calibrations must satisfy the following criteria:

1. **Out-of-Sample Validation:** Calibration performed on training windows (e.g., 1980–2005) must accurately forecast out-of-sample test regimes (e.g., 2006–2025) with a Mean Absolute Percentage Error (MAPE) $< 8\%$.
2. **Exclusion of Headline CPI:** Submissions utilizing aggregate consumer price indices rather than raw physical survival baskets ($C_{surv\_std}$) will be rejected automatically.
3. **Information Criteria Testing:** Any proposed addition of polynomial terms or supplemental variables must demonstrate superior Akaike Information Criterion (AIC) and Bayesian Information Criterion (BIC) scores relative to the base 4PL formulation.
