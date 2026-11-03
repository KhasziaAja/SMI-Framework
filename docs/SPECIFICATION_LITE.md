# SMI Framework: Layer 1 Mathematical Specification (SPECIFICATION_LITE) - v1.0

[English](./SPECIFICATION_LITE.md) | [日本語](./SPECIFICATION_LITE.ja.md)

> **"Individual behavioral choice is governed not by subjective utility, but by physical constraints on real disposable metabolic margin (a dimensionless ratio) after unavoidable fixed costs are deducted."**

## 1. Operational Preconditions & Boundary Conditions

This mathematical framework is not an unconstrained, universal abstraction applicable to all historic or tribal ecosystems. It is a deterministic physical model calibrated exclusively for modern urban capitalist social systems. To guarantee scientific falsifiability and prevent model misapplication, the following three structural boundary conditions define the mandatory runtime environment:

### 1.1 Precondition 1: Monetized Market Economy

The overwhelming majority of an individual's essential survival and reproductive fixed overhead (housing, nutrition, critical utilities, education, statutory taxation, and social insurance) must be procured through competitive markets and settled in fiat currency.

* **Out of Scope:** Purely subsistence agrarian barter economies, or command economies (such as the former Soviet Union) where residential housing, utilities, and healthcare were allocated as unpriced public state quotas. In these ecologies, the denominator as a market-clearing price is distorted or absent.

### 1.2 Precondition 2: Individual Autonomy & Reproductive Choice

Individuals possess full legal, statutory, and cultural rights over marriage, singlehood, contraception, and personal lifestyle choices.

* **Out of Scope:** Slave-based economies, compulsory state-mandated marriage, or closed patriarchal communities enforced by religious dogma where reproduction is non-consensual. Under such environments, the prefrontal neural survival brake is physically overridden, causing a phase shift from human behavioral economics into an agricultural livestock model.

### 1.3 Precondition 3: Offspring as Net Economic Liabilities ($P_{net} < 1.0$)

Under statutory child-labor bans, mandatory public schooling, and advanced knowledge-economy labor markets, dependent children represent a structural net financial liability for 18–22 years, unable to contribute labor or income to parental cash flow.

* **Out of Scope:** Pre-industrial agrarian societies where children contribute directly to household agrarian labor from early childhood, creating a dynamic where reproduction yields a positive net economic return ($P_{net} > 1.0$).

## 2. Base Formulation & Variable Definitions

This section defines the mathematical formulations, data schemas, transfer functions, and normalization plug-ins for the primary public protocol (SMI Lite Standard) within qualified modern market societies.

### 2.1 Base Dimensionless Equation

For any discrete spatial mesh or cohort $i$ at time $t$, the **Social Margin Index (SMI)** is defined as:

$$
SMI_{i, t} = \frac{WCI_{i, t}}{C_{surv\_std}(i, t)}
$$

* **Output** $SMI_{i, t} \in \mathbb{R}^+$: Dimensionless scalar multiplier independent of currency unit or nominal inflation.

* **Numerator** $WCI_{i, t}$ **(Working Capital Income)**: Median real disposable take-home pay of prime young singles (ages 25–34), net of income taxes and mandatory social contributions.

* **Denominator** $C_{surv\_std}(i, t)$ **(Standard Survival Cost)**: Unavoidable baseline fixed overhead required to maintain continuous economic participation and baseline reproductive solvency.

### 2.2 Anatomical Decomposition of $C_{surv\_std}$: Absolute vs. Quasi-Fixed Costs

Restricting the denominator strictly to public assistance minimum subsistence budgets or bare biological caloric floors yields distorted scores: a nominal income of $WCI \approx \$2,000/\text{month}$ evaluated against a baseline physiological cost of $\$1,400$ produces an apparent $SMI \approx 1.43$. This generates an empirical paradox where populations appear fiscally solvent, yet marriage rates and total fertility crash toward zero.

To resolve this measurement failure, the denominator is decoupled into **Absolute Fixed Survival Costs** and **Quasi-Fixed Systemic Drag**:

$$
C_{surv\_std} = C_{base} + C_{semi}
$$

$$
C_{base} = C_{rent} + C_{food\_min} + C_{infra\_vital}
$$

$$
C_{semi} = C_{tax\_ins} + C_{depr} + C_{conn} + (\theta \cdot R_{rel})
$$

> **【Exclusion of General Headline CPI Deflators】**
>
> This framework explicitly rejects nominal adjustments via official headline Consumer Price Index (CPI) baskets. CPI series are systematically dampened by hedonic quality adjustments in non-essential durable consumer tech (electronics, TVs, computers) that mask acute inflation across non-negotiable living overhead. SMI enforces an **unhedged physical basket restricted to the four non-negotiable survival pillars: median market rent, statutory payroll drag, lifeline utilities, and structural education/depreciation reserves**.

#### Variable Definitions & Empirical Sources

| Notation | Variable Parameter | Definition & Empirical Threshold | Primary Data Sources (OECD / US / JP) | 
| ----- | ----- | ----- | ----- | 
| $C_{rent}$ | Market-Clearing Rent | Median private market rent for standard 25–30 sqm single-occupancy unit (excl. subsidized housing) | Census Bureau ACS, HUD Fair Market Rents, Housing Portal APIs | 
| $C_{food\_min}$ | Essential Caloric Baseline | Self-prepared nutritional baseline satisfying required caloric and macro balances | National Household Budget Surveys (Food Component) | 
| $C_{infra\_vital}$ | Lifeline Utility Drag | Electricity, water, gas, and basic municipal sewage overhead | Utility regulatory filings, Household Expenditure Surveys | 
| $C_{tax\_ins}$ | Statutory Marginal Drag | Non-discretionary payroll taxes, pension contributions, and mandatory public health levies | National Tax/Treasury Schedules, OECD Taxing Wages | 
| $C_{depr}$ | Self-Capital Sinking Fund | Monthly amortized provision for domestic appliance wear, security deposits, and preventive health | Family Income and Expenditure Surveys | 
| $C_{conn}$ | Digital Connectivity | Minimum high-speed data line and baseline mobile smartphone operational cost | Median national telecom plan pricing | 
| $\theta \cdot R_{rel}$ | Relative Positional Drag | Community-enforced positional cost required to prevent socioeconomic isolation and educational exclusion | Ministry of Education Surveys, Regional Gini Coefficients | 

> **【Mathematical Demonstration: The Vertical Descent Under Quasi-Fixed Costs】**
>
> Given net monthly take-home $WCI = \$2,000$:
>
> * Evaluating Absolute Costs Only: $C_{base} = \$650 (\text{Rent}) + \$350 (\text{Food}) + \$120 (\text{Utilities}) = \$1,120$
>
>   $$
>   \to SMI_{base} = \frac{\$2,000}{\$1,120} \approx 1.78 \quad \text{(Illusion of solvency and reproductive capacity)}
>   $$
>
> * Incorporating Quasi-Fixed Overhead: $C_{semi} = \$450 (\text{Payroll Drag}) + \$200 (\text{Sinking Fund}) + \$100 (\text{Telecom}) + \$250 (\text{Positional/Education Drag}) = \$1,000$
>
>   $$
>   C_{surv\_std} = \$1,120 + \$1,000 = \$2,120
>   $$
>
>   $$
>   \to SMI = \frac{\$2,000}{\$2,120} \approx 0.94 \quad \text{(Breaches self-sustenance limit into involuntary shutdown)}
>   $$
>
> Ignoring quasi-fixed overhead leaves macro models blind to an individual's chronic capital depletion.

### 2.3 Positional Standard Cost Formulation ($R_{rel}$)

Sub-replacement fertility in advanced economies is driven not merely by absolute physiological deprivation, but by the structural escalation of positional baseline costs. This is formalized via the following plug-in function:

$$
R_{rel} = \frac{Median(Edu_{local}) + Gini_{region} \cdot C_{base}}{C_{base}}
$$

* $Median(Edu_{local})$: Median monthly expenditure on private shadow education, tutoring, and test preparation within the local mesh.

* $Gini_{region}$: Regional Gini coefficient (higher inequality magnifies positional and status signaling competition).

* $\theta \in [0.0, 1.0]$: Cultural normative sensitivity index ($\theta \to 1.0$ in high-conformity societies like East Asia; $\theta \to 0.2$ in individualist contexts).

### 2.4 Dual-Income Household Time-Deficit Correction Model

Summing dual incomes without accounting for lost domestic production hours distorts real margin by overlooking outsourced domestic costs and cognitive exhaustion (The 1.5-Earner Trap).

Household evaluation therefore applies a time-decay discount to aggregate earnings:

$$
WCI_{eff} = \frac{WCI_1 + WCI_2}{1 + \lambda \cdot \max\left(0, \frac{H_1 + H_2 - H_{standard}}{H_{standard}}\right)}
$$

* $H_1, H_2$: Total monthly hours worked per partner (including overtime and transit).

* $H_{standard}$: Standard statutory monthly hours threshold (e.g., 160 hours/month).

* $\lambda \approx 0.35$: Time-depletion penalty coefficient (converting lost domestic labor into externalized services, commercial meals, and burnout drag).

## 3. Non-linear TFR Transfer Function (4PL Logistic Model)

The empirical response of total fertility (TFR) to changes in SMI is not linear. It follows a **4-Parameter Logistic (4PL) Sigmoid Function**, capturing biological safety thresholds and asymptotic ecological carrying capacity:

### 3.1 Transfer Function Formulation

$$
TFR(SMI) = TFR_{min} + \frac{TFR_{max} - TFR_{min}}{1 + \left(\frac{SMI}{SMI_0}\right)^{-k}}
$$

```
    TFR
     ^
TFRmax |---------------------------------------*** (Upper Carrying Capacity)
       |                                   ***
       |                                ** 
       |                              ** (Steep Phase Shift: Goldilocks Zone 1.40)
       |                           **
       |                         *
       |                       * (Inflection Point SMI_0 ≈ 1.05)
TFRmin |--------------------***
       +---------------------------------------------> SMI
       0                   0.60   1.00  1.40    2.07

```

### 3.2 Calibrated Parameter Thresholds & Empirical Rationale

| Parameter | Calibrated Value | Physical & Evolutionary Rationale | 
| ----- | ----- | ----- | 
| $TFR_{min}$ | $0.65 \pm 0.05$ | Biological lower floor under extreme economic compression ($SMI \to 0$, as observed in Seoul) | 
| $TFR_{max}$ | $2.15 \pm 0.10$ | Asymptotic social carrying capacity in modern urban economies (just above replacement level) | 
| $SMI_0$ | $1.05 \pm 0.03$ | Curve inflection point where neurobiological reproductive inhibition begins lifting | 
| $k$ | $4.00 \pm 0.25$ | Slope sensitivity factor (equivalent to the Hill coefficient), dictating rapid phase shifts near thresholds | 

### 3.3 Marginal Sensitivity Function

The first derivative $\frac{d(TFR)}{d(SMI)}$ defines the policy efficiency spectrum:

$$
\frac{d(TFR)}{d(SMI)} = \frac{k \cdot (TFR_{max} - TFR_{min}) \cdot \left(\frac{SMI}{SMI_0}\right)^{-(k+1)}}{SMI_0 \cdot \left[1 + \left(\frac{SMI}{SMI_0}\right)^{-k}\right]^2}
$$

* $SMI < 0.80$: Marginal elasticity nears zero (token cash grants produce zero measurable demographic response).

* $SMI \approx 1.05$: Elasticity reaches its global maximum (highest marginal return per unit of overhead reduction).

* $SMI > 1.80$: Marginal returns decay asymptotically toward $TFR_{max}$, resolving the high-earner demographic paradox.

## 4. Distributed Lag Impulse Model

The temporal delay connecting input shifts ($SMI$) to output shifts ($TFR$) is modeled as an **empirical 3-to-5-year distributed lag convolution**, reflecting courtship, pair-bonding, and gestation cycles:

### 4.1 Discrete Finite Impulse Response (FIR)

$$
TFR_t = \sum_{\tau=3}^{5} w_\tau \cdot \Phi(SMI_{t-\tau})
$$

$$
\Phi(SMI) = 4PL(SMI)
$$

$$
\sum_{\tau=3}^{5} w_\tau = 1.0, \quad w_\tau > 0
$$

### 4.2 Standard Lag Weight Allocation

Calibrated via distributed lag econometric modeling and adult mammalian life-history invariants (\~5% of adult lifespan):

$$
\mathbf{w} = \begin{bmatrix} w_3 \\ w_4 \\ w_5 \end{bmatrix} = \begin{bmatrix} 0.20 \\ 0.65 \\ 0.15 \end{bmatrix}
$$

* $\tau = 4$ (4-year latency) constitutes the dominant primary peak ($65\%$ aggregate weight).

* Granger causality tests confirm $SMI_{t-4} \to TFR_t$ statistical significance at $p < 0.001$.

## 5. International Normalization Plug-in Architecture

To maintain the universality of the core dimensionless engine without distorting institutional tax and welfare divergence across jurisdictions, modular normalization plug-ins interface with local data schemas:

```
       [ National Administrative Datasets / Jurisdictional Rules ]
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────────────┐
│                   Normalization Plug-in Layer                       │
│  - Nordic/France: Universal In-Kind Childcare, APL Housing Subsidies│
│  - US: Private Health Deductibles, Federal/Private Student Debt     │
│  - South Korea: Jeonse Capital Opportunity Costs, Hagwon Overhead   │
└─────────────────────────────────────────────────────────────────────┘
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────────────┐
│          SMI Core Engine (Layer 1 Dimensionless Protocol)           │
│                       SMI = WCI / C_surv_std                        │
└─────────────────────────────────────────────────────────────────────┘

```

### 5.1 Nordic / French Plug-in (Universal In-Kind Transfers & Co-habitation)

Adjusts for statutory child care allowances, subsidized housing vouchers (APL), and legal protections for civil unions (PACS):

$$
C_{surv\_nordic} = (C_{base} + C_{semi}) \cdot (1 - S_{gov}) \cdot \phi_{legal}
$$

* $S_{gov} \in [0.0, 0.5]$ **(Public Transfer Offset)**: Deducts cash-equivalent values of public daycare, child benefits, and housing allowances directly from living overhead.

* $\phi_{legal} \approx 0.88$ **(Union Friction Reducer)**: Accounts for the minimization of institutional costs associated with marriage through parity in civil unions.

### 5.2 United States Plug-in (Private Healthcare, Student Loans & Quintile Separation)

Evaluates income quintiles ($Q_1 - Q_5$) independently, adding mandatory private health premiums, out-of-pocket deductibles, and non-dischargeable education debts:

$$
C_{surv\_us}(Q_k) = C_{base}(Q_k) + C_{semi}(Q_k) + C_{health\_private} + C_{student\_debt}
$$

* $C_{health\_private}$: Mean monthly out-of-pocket health insurance premium plus amortized deductible.

* $C_{student\_debt}$: Mandatory monthly amortized payments on federal and private tertiary education loans.

* Captures the bifurcated demographic reality where $Q_1, Q_2$ are crushed below $0.50$, while $Q_5$ operates above $2.50$.

### 5.3 South Korea Plug-in (Jeonse Deposit Capital Drag & Shadow Education)

Addresses structural housing dynamics (Jeonse lump-sum lease deposits) and hyper-competitive private schooling expenditures:

$$
C_{surv\_kr} = C_{base} + C_{semi} + \text{OpportunityCost}(Jeonse) + (\theta_{kr} \cdot R_{rel})
$$

* $\text{OpportunityCost}(Jeonse)$: Capital financing costs (or forfeited investment yields) tied up in multi-hundred-thousand-dollar residential deposit commitments.

* $\theta_{kr} \to 1.0$: Universalizes private tutoring (Hagwon) expenditures as compulsory social participation overhead.

## 6. Input/Output Data Schema (JSON Schema v7 Reference)

Full technical specification for the Layer 1 operational input pipeline:

```
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "SMILayer1InputSchema",
  "type": "object",
  "required": [
    "region_metadata",
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
    "economic_inputs": {
      "type": "object",
      "required": ["wci_single_median", "currency_unit"],
      "properties": {
        "wci_single_median": { "type": "number", "minimum": 0 },
        "household_dual_income": { "type": "number", "default": 0 },
        "weekly_work_hours_total": { "type": "number", "default": 40 },
        "currency_unit": { "type": "string" }
      }
    },
    "survival_cost_components": {
      "type": "object",
      "required": [
        "c_rent_median",
        "c_food_essential",
        "c_infra_utilities",
        "c_tax_and_social_insurance",
        "c_depreciation_reserve",
        "c_connectivity"
      ],
      "properties": {
        "c_rent_median": { "type": "number", "minimum": 0 },
        "c_food_essential": { "type": "number", "minimum": 0 },
        "c_infra_utilities": { "type": "number", "minimum": 0 },
        "c_tax_and_social_insurance": { "type": "number", "minimum": 0 },
        "c_depreciation_reserve": { "type": "number", "minimum": 0 },
        "c_connectivity": { "type": "number", "minimum": 0 },
        "relative_cost_factor": { "type": "number", "default": 0.0, "minimum": 0.0, "maximum": 1.0 }
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

## 7. Operational Guidelines & Engine Deployment

The mathematical formulations standardized in Layer 1 shift public policy evaluations away from superficial cash subsidies toward structural overhead reduction:

1. **Automated Pipeline Integration:** Build automated ETL workers mapping official statistical APIs (e-Stat, OECD.Stat, Eurostat, US BLS) directly into the standardized JSON input schema.

2. **Empirical Curve Calibration:** Leverage spatial mesh cohorts to continuously optimize the logistic Hill coefficient $k$ and empirical delay vector $\mathbf{w}$.

3. **Core Layer Interface:** Output scalar metrics ($SMI_{i, t}$) pass directly as uncompressed baseline vectors into `SPECIFICATION_CORE.md` for spatial friction, migration tipping points, and defense intake horizon forecasting.
