# SMI Framework: Layer 1 Mathematical Specification (SPECIFICATION_LITE) - v1.1

[English](./SPECIFICATION_LITE.md) | [日本語](./SPECIFICATION_LITE.ja.md)

> **"Individual behavioral choice is governed not by subjective utility, but by physical constraints on real disposable metabolic margin (a dimensionless ratio) after unavoidable fixed costs are deducted."**

## 1. Operational Preconditions & Boundary Conditions

This mathematical framework is not an unconstrained, universal abstraction applicable to all historic or tribal ecosystems. It is a deterministic physical model calibrated exclusively for modern urban capitalist social systems. To guarantee scientific falsifiability and prevent model misapplication, the following three structural boundary conditions define the mandatory runtime environment:

### 1.1 Precondition 1: Monetized Market Economy

The primary survival and reproductive overheads (housing, nutrition, vital utilities, education, taxation, and social security) must be settled predominantly via fiat currency within open market transactions.

* **Out of Scope:** Subsistence agrarian communes or command economies with universal state rationing of housing, food, and medical care (e.g., Soviet-style systems), where market-clearing survival denominators do not exist or are heavily distorted.

### 1.2 Precondition 2: Individual Autonomy & Free Will

Individual actors (both sexes) must possess legally and institutionally guaranteed autonomy regarding marriage, cohabitation, contraception, and lifestyle choices.

* **Out of Scope:** Chattel slavery, forced marital arrangements, or closed patriarchal/theocratic enclaves where reproductive autonomy is coercively overridden. In such regimes, prefrontal executive survival brakes are externally bypassed, transitioning the system from a human bio-economic model (SMI) to an agricultural/livestock management model.

### 1.3 Precondition 3: Structural Child Net Cost ($P_{net} < 1.0$)

Due to child labor prohibitions, compulsory schooling, and urban industrial labor markets, offspring must function strictly as net economic liabilities (fixed overhead) until adulthood (ages 18–22), rather than immediate household revenue generators.

* **Out of Scope:** Pre-industrial agrarian regimes where children contribute productive agricultural labor from early childhood, yielding positive net household returns per birth ($P_{net} > 1.0$).

## 2. Core Equation & Engineering Variable Definitions

This section formalizes the mathematical structure, variable types, transfer functions, and normalization protocols for Layer 1 (**SMI Lite Standard**) within urban capitalist environments.

### 2.1 Base Dimensionless Equation

For a given spatial mesh or demographic cohort $i$ at time $t$, the **Social Margin Index (SMI)** is defined as:

$$
SMI_{i, t} = \frac{WCI_{i, t}}{C_{surv\_std}(i, t)}
$$

* **Output** $SMI_{i, t} \in \mathbb{R}^+$: A dimensionless scalar ratio independent of currency units or nominal price inflation.

* **Numerator** $WCI_{i, t}$ **(Working Capital Income)**: Median real net disposable income of young single adults (ages 25–34) after mandatory income taxes, municipal taxes, and statutory social security withholdings.

* **Denominator** $C_{surv\_std}(i, t)$ **(Standard Survival Cost)**: Standardized fixed overhead required to maintain physiological health, social participation, and reproductive viability.

### 2.2 Universal Phase Transition Thresholds & The Labor Market Floor Constant

The resulting dimensionless scalar $SMI$ mechanically classifies bio-social regimes across five universal phase thresholds, invariant across nations and historical eras:

| SMI Range / Threshold | Regime Status | Physical & Bio-Social System State | 
| ----- | ----- | ----- | 
| $\ge 2.07$ | **Replacement Boost Zone** | Total Fertility Rate (TFR) stably exceeds population replacement ($\approx 2.07$), driving organic demographic expansion. | 
| $1.40$ | **Household Formation Golden Zone** | Equilibrium cruising altitude aligned with OECD equivalence scales ($+0.5$ additional adult, $+0.3$ per child). | 
| $1.00$ | **Unloaded Break-Even Line** | Single individual barely achieves cash-flow equilibrium inclusive of depreciation reserves (zero shock buffer). | 
| $< 0.60$ | **Autonomic Shutdown / Cannibalization** | Prefrontal executive defense brakes engage; individuals liquidate future depreciation/health reserves while ceasing reproduction. | 
| $\approx 0.45$ | **Labor Market Floor Constant** | Empirical physical lower bound ($0.44 \sim 0.53$) observed consistently across structurally divergent advanced economies (Japan, US, Sweden, Italy, Hungary) for populations remaining in formal self-supporting labor (Track A). Compression below this floor forces phase transition into public assistance dependency (Track B) or underground/high-friction instability ($\text{Toxicity}$). | 

### 2.3 Anatomy of the Denominator $C_{surv\_std}$: Absolute vs. Quasi-Fixed Overhead

If only public welfare minimums (subsistence poverty lines) are entered into the denominator, an individual earning $WCI \approx ¥200,000$ against bare subsistence costs of $¥140,000\text{–}150,000$ yields an apparent $SMI \approx 1.3\text{–}1.4$. This generates severe statistical deception: individuals appear financially viable on paper while marriage and birth rates collapse in reality.

To eliminate this distortion, $C_{surv\_std}$ is strictly formulated as the linear sum of **Absolute Fixed Costs** and **Quasi-Fixed Social Survival Costs**:

$$
C_{surv\_std} = C_{base} + C_{semi}
$$

$$
C_{base} = C_{rent} + C_{food\_min} + C_{infra\_vital}
$$

$$
C_{semi} = C_{tax\_ins} + C_{depr} + C_{conn} + (\theta \cdot R_{rel})
$$

> **【Intentional Exclusion of Headline CPI Deflation】**
>
> The denominator ($C_{surv\_std}$) intentionally rejects deflation via official headline Consumer Price Indices (CPI). Headline CPI masks acute survival inflation through hedonic price drops in consumer electronics (TVs, PCs). Instead, SMI evaluates a direct physical basket of the four unavoidable biological overheads: urban market rent, marginal tax/social insurance wedges, essential utilities, and preventative health/depreciation reserves.

#### Component Specifications & Statistical Mapping

| Variable | Component Name | Operational Definition & Inclusion Criteria | Primary Statistical Sources (JP / US / OECD) | 
| ----- | ----- | ----- | ----- | 
| $C_{rent}$ | Median Market Rent | Median private-sector rent for standard single-occupancy floor area (25–30 $\text{m}^2$), excluding subsidized public housing. | e-Stat Housing Survey, Commercial Rental APIs, HUD FMR | 
| $C_{food\_min}$ | Essential Nutrition | Baseline home-prepared caloric and macronutrient maintenance cost. | Household Budget Survey (Basic Food Expenditure) | 
| $C_{infra\_vital}$ | Vital Utilities | Unavoidable electricity, water, and heating/gas expenditures. | Household Budget Survey (Utilities) | 
| $C_{tax\_ins}$ | Marginal Public Wedge | Statutory payroll deductions (income tax, local tax, public pension, mandatory health insurance). | National Tax/Social Insurance Tables, US CPS | 
| $C_{depr}$ | Defensive Depreciation | Monthly amortized reserve for appliance replacement, lease renewals, ceremonial obligations, and preventative care. | National Survey of Family Income and Expenditure | 
| $C_{conn}$ | Employment Connectivity | Essential mobile data plan and smartphone hardware amortization required for modern labor participation. | Median Telecom Expenditure Benchmarks | 
| $\theta \cdot R_{rel}$ | Relative Status Overhead | Local social conformity, status signaling, and private educational arms-race costs required to avoid community exclusion. | Private Education Expenditure Surveys, Regional Gini | 

> **【Mathematical Proof: Why Quasi-Fixed Costs Trigger Vertical SMI Collapse】**
>
> Given a monthly net income $WCI = ¥200,000$:
>
> * **Absolute Fixed Costs Only:** $C_{base} = 65,000(\text{Rent}) + 35,000(\text{Food}) + 12,000(\text{Utilities}) = ¥112,000$
>
>   $$
>   \to SMI_{base} = \frac{200,000}{112,000} \approx 1.78 \quad \text{(Illusion of reproductive viability)}
>   $$
>
> * **Inclusive of Quasi-Fixed Overhead:** $C_{semi} = 45,000(\text{Tax/Ins}) + 20,000(\text{Depreciation}) + 10,000(\text{Telecom}) + 25,000(\text{Status/Health}) = ¥100,000$
>
>   $$
>   C_{surv\_std} = 112,000 + 100,000 = ¥212,000
>   $$
>
>   $$
>   \to SMI = \frac{200,000}{212,000} \approx 0.94 \quad \text{(Drops below 1.00 break-even into autonomic shutdown)}
>   $$
>
> Official statistics ignoring quasi-fixed costs fail to detect the continuous liquidation of future human capital ("invisible bleeding").

### 2.4 Relative Standard Cost Formulation ($R_{rel}$)

Fertility collapse in advanced economies is driven not by absolute starvation, but by localized cost inflation via peer comparison. This is modeled as an endogenous plug-in term:

$$
R_{rel} = \frac{Median(Edu_{local}) + Gini_{region} \cdot C_{base}}{C_{base}}
$$

* $Median(Edu_{local})$: Local spatial mesh median expenditure on private cram schools, tutoring, and extracurricular arms races.

* $Gini_{region}$: Regional income Gini coefficient (higher local inequality amplifies status-defense spending).

* $\theta \in [0.0, 1.0]$: Cultural conformity sensitivity parameter ($\theta \to 1.0$ in high-conformity East Asian urban centers; $\theta \to 0.2$ in individualistic regimes).

### 2.5 Dual-Income Household Time-Compression Adjustment

Summing dual household incomes ($WCI_1 + WCI_2$) without adjusting for lost domestic/childcare hours artificially inflates household SMI ("The 1.5-Horsepower Trap"). Effective household $WCI_{eff}$ applies a time-depletion decay factor:

$$
WCI_{eff} = \frac{WCI_1 + WCI_2}{1 + \lambda \cdot \max\left(0, \frac{H_1 + H_2 - H_{standard}}{H_{standard}}\right)}
$$

* $H_1, H_2$: Total monthly working hours (including overtime and commuting) for each partner.

* $H_{standard}$: Statutory standard monthly working hours (e.g., 160 hours/month).

* $\lambda \approx 0.35$: Time-depletion penalty coefficient converting lost domestic capacity into outsourced childcare, prepared food, and cognitive fatigue costs.

## 3. Dual-Lens Observation Specification: Standard Lens & Canary Model

The SMI Framework preserves a single invariant core equation ("the camera body") while switching input quantile filters ("the optical lenses") to capture both macro demographic trajectories and early-warning structural decay:

```
┌─────────────────────────────────────────────────────────────────────┐
│                 Input Filter Layer (Optical Lenses)                 │
│  [Standard Lens: Median (P50)]    [Canary Lens: Lower Q25–Q40]      │
└──────────────────┬──────────────────────────────────┬───────────────┘
                   │                                  │
                   ▼                                  ▼
┌─────────────────────────────────────────────────────────────────────┐
│          SMI Core Engine (Invariant Dimensionless Formula)          │
│                   SMI_{i, t} = WCI_{i, t} / C_{surv\_std}           │
└──────────────────┬──────────────────────────────────┬───────────────┘
                   │                                  │
                   ▼                                  ▼
        [Macro TFR Trajectory]             [12–15 Yr Early Warning]
      (3–5 Year Distributed Lag)         (Floor Compression & Friction)
```

### 3.1 Standard Lens ($SMI_{std}$: Population Median P50)

* **Target Cohort:** Young adults aged 25–34 at the **50th percentile (Median)** of Track A earnings.

* **Analytical Function:** Governs aggregate national/regional TFR trajectories via the 3–5 year distributed lag transfer function (Section 4).

### 3.2 Canary Lens ($SMI_{canary}$: Lower-Tier Working Cohort Q25–Q40)

* **Target Cohort:** Young adults aged 25–34 in the **25th to 40th income percentiles** (lower-tier regular and non-regular formal workers).

* **Lead-Time Invariant (12–15 Year Early Warning):** Because lower-tier workers possess zero asset buffers, their disposable margin compresses first. Empirical cross-national backtesting confirms that $SMI_{canary}$ breaches the $0.60$ shutdown threshold and hits the $\approx 0.45$ Labor Market Floor **12 to 15 years prior** to median middle-class collapse.

* **Cross-Layer Coupling Trigger:** When $SMI_{canary}$ remains pinned at the $\approx 0.45$ floor, formal labor participation breaks down, serving as a leading macro-trigger for non-linear social friction ($\text{Toxicity}$) and public order degradation modeled in Layer 2 (`SPECIFICATION_CORE.md`).

## 4. Non-Linear TFR Transfer Function & Distributed Lag Model

### 4.1 4-Parameter Logistic (4PL) Sigmoid Response

Demographic fertility does not respond linearly to income increases; it exhibits threshold activation and biological upper saturation (the "affluent fertility plateau"). The steady-state fertility response $f(SMI)$ is modeled as a 4PL Hill-type sigmoid function:

$$
f(SMI) = TFR_{min} + \frac{TFR_{max} - TFR_{min}}{1 + \left(\frac{SMI}{SMI_0}\right)^{-k}}
$$

* $TFR_{min} \approx 0.65$: Biological floor under extreme survival compression (ultra-low urban fertility).

* $TFR_{max} \approx 2.35$: Asymptotic upper ceiling constrained by biological gestation limits and modern lifestyle saturation.

* $SMI_0 \approx 1.05$: Inflection point where reproductive suppression rapidly unlocks.

* $k \approx 4.0$: Hill steepness parameter governing phase transition sensitivity.

### 4.2 Distributed Lag Convolution Kernel (3–5 Year Bio-Clock)

Consistent with K-selected mammalian life-history invariants (where gestation, pair-bonding, and environmental verification require $\approx 5\%$ of adult lifespan), observed $TFR_t$ is governed by a finite impulse response (FIR) distributed lag convolution over $t-3$ to $t-5$ years:

$$
TFR_t = \sum_{k=3}^{5} w_k \cdot f(SMI_{t-k}) \quad \text{subject to} \quad \sum_{k=3}^{5} w_k = 1
$$

* **Standard Empirical Weight Vector:** $\mathbf{w} = [w_3, w_4, w_5] = [0.20, 0.65, 0.15]$, peaking sharply at $t - 4$ years.

## 5. International Normalization Plug-in & Dual-Track Separation

To apply the invariant threshold scale ($0.45 / 0.60 / 1.00 / 1.40 / 2.07$) across divergent welfare and institutional regimes without altering the core equation, national data pipelines must execute two normalization protocols:

### 5.1 Dual-Track Institutional Separation (Track A vs. Track B)

Mixing self-supporting taxpayers with public-assistance recipients corrupts quantile distributions and masks lower-tier collapse. All national pipelines must segregate cohorts into two tracks prior to computing $SMI$:

* **Track A (Self-Supporting Labor Cohort):** Individuals funding housing, taxation, and survival overhead directly through market wages. Both Standard ($P50$) and Canary ($Q25\text{–}Q40$) lenses are evaluated strictly within Track A.

* **Track B (Public Transfer / Exempt Cohort):** Individuals receiving full housing vouchers, tax/social-insurance exemptions, or cash welfare where market denominators are administratively neutralized. Track B is tracked separately to prevent artificial statistical distortion of Track A floor dynamics.

### 5.2 Jurisdictional Plug-in Adjustments

$$
SMI_{norm} = \frac{WCI_{gross} - C_{tax\_ins} - C_{debt\_edu} + B_{cash\_universal}}{C_{base} + C_{semi} - S_{gov\_inkind}}
$$

* **Nordic / Continental Europe ($S_{gov\_inkind}$):** Universal in-kind childcare, free tertiary education, and housing allowances (e.g., French APL) are deducted directly from the denominator $C_{surv\_std}$.

* **United States ($C_{debt\_edu}, C_{health\_priv}$):** Private health insurance premiums/deductibles and federal/private student loan servicing are explicitly added to $C_{semi}$.

* **East Asia ($\theta \to 1.0$):** High private cram-school arms races ($Median(Edu_{local})$) and housing deposit opportunity costs (e.g., South Korean *Jeonse* capital lock-up) are capitalized into $C_{semi}$.

## 6. Input/Output Data Schema (JSON Schema Draft-07 Reference)

Standardized I/O schema for automated ETL pipelines and cross-layer coupling (v1.1):

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "SMILayer1InputSchema_v1_1",
  "type": "object",
  "required": [
    "region_metadata",
    "observation_lens",
    "economic_inputs",
    "survival_cost_components",
    "time_series_lag_weights"
  ],
  "properties": {
    "region_metadata": {
      "type": "object",
      "required": ["country_iso", "mesh_id", "year"],
      "properties": {
        "country_iso": { "type": "string", "pattern": "^[A-Z]{3}$" },
        "mesh_id": { "type": "string" },
        "year": { "type": "integer", "minimum": 1950, "maximum": 2100 }
      }
    },
    "observation_lens": {
      "type": "object",
      "required": ["lens_type", "cohort_track"],
      "properties": {
        "lens_type": { "type": "string", "enum": ["STANDARD_P50", "CANARY_Q25_40"] },
        "cohort_track": { "type": "string", "enum": ["TRACK_A_MARKET", "TRACK_B_TRANSFER"] }
      }
    },
    "economic_inputs": {
      "type": "object",
      "required": ["wci_single_net", "currency_unit"],
      "properties": {
        "wci_single_net": { "type": "number", "minimum": 0 },
        "household_dual_net": { "type": "number", "default": 0 },
        "monthly_work_hours_total": { "type": "number", "default": 160 },
        "currency_unit": { "type": "string" }
      }
    },
    "survival_cost_components": {
      "type": "object",
      "required": [
        "c_rent_median",
        "c_food_min",
        "c_infra_vital",
        "c_tax_ins",
        "c_depr",
        "c_conn"
      ],
      "properties": {
        "c_rent_median": { "type": "number", "minimum": 0 },
        "c_food_min": { "type": "number", "minimum": 0 },
        "c_infra_vital": { "type": "number", "minimum": 0 },
        "c_tax_ins": { "type": "number", "minimum": 0 },
        "c_depr": { "type": "number", "minimum": 0 },
        "c_conn": { "type": "number", "minimum": 0 },
        "r_rel_factor": { "type": "number", "default": 0.0, "minimum": 0.0 },
        "theta_conformity": { "type": "number", "default": 0.5, "minimum": 0.0, "maximum": 1.0 },
        "s_gov_inkind_deduction": { "type": "number", "default": 0.0, "minimum": 0.0 }
      }
    },
    "time_series_lag_weights": {
      "type": "object",
      "required": ["w3", "w4", "w5"],
      "properties": {
        "w3": { "type": "number", "default": 0.20 },
        "w4": { "type": "number", "default": 0.65 },
        "w5": { "type": "number", "default": 0.15 }
      }
    }
  }
}
```

## 7. Operational Guidelines & Downstream Coupling

1. **Automated ETL Ingestion:** Data pipelines must map primary administrative tables (e-Stat, US CPS, Eurostat, OECD.Stat) directly into the Track A / Track B JSON schema without headline CPI deflators.
2. **Empirical Parameter Calibration:** Contributors are invited to submit regional fits for Hill steepness $k$, conformity sensitivity $\theta$, and Canary lead-time vectors via repository discussions.
3. **Layer 2 Core Coupling:** Both $SMI_{std}$ and $SMI_{canary}$ scalar outputs pass directly as uncompressed baseline vectors into `SPECIFICATION_CORE.md` to evaluate non-linear spatial friction ($\text{Toxicity}$), phase separation thresholds, and 20-year sovereign intake trajectories.
