# SMI Framework (Social Margin Index) - v1.0 [Open Standard]

[English](./README.md) | [日本語](./README.ja.md)

> **"The survival or collapse of human civilization is governed not by moral narratives or cultural values, but by physical constraints on real disposable metabolic margin (SMI)."**

The SMI Framework is an open-source, socioeconomic engineering protocol (State OS Core Architecture) designed to model, diagnose, and simulate individual bioenergetic disposable margins, population replenishment dynamics, and systemic civilizational phase transitions.

---

## 1. System Philosophy & Operational Boundary Conditions

### 1.1 Philosophy: Releasing the Autonomic Shutdown
In contemporary post-industrial and urbanized societies, collapsing fertility rates and plunging marriage numbers are routinely dismissed through moralizing cultural narratives—such as "young generations losing romantic interest," "lifestyle diversification," or "decaying civic responsibility."

The SMI Framework rejects these unquantifiable psychological rationalizations.

*Homo sapiens*, as large mammals operating under an evolutionary K-strategy, possess hardwired homeostatic fail-safes. When unavoidable fixed survival overhead—market rent, statutory payroll drag, lifeline utilities, and structural education costs—exceeds real disposable caloric/capital intake, the organism's prefrontal cortex locks into an **Autonomic Shutdown (reproductive and long-term investment cessation)** to protect immediate physiological survival.

Sub-replacement fertility is not a moral failure; it is an involuntary, biological emergency brake triggered by depleted resource margins.

```text
┌────────────────────────────────────────────────────────────────────────┐
│               Macro-Socioeconomic System Dynamics                      │
└──────────────────────────────────┬─────────────────────────────────────┘
                                   │
         ┌─────────────────────────┴─────────────────────────┐
         ▼                                                   ▼
【Channel A: Industrial/Market Economy】             【Channel B: Biological/Civic Margin】
 (CPU Clock Rate / Thermal Output)                  (Power Supply Voltage / Cooling Margin)
 · Metrics: GDP, Equity Indices, Corporate Profits  · Metrics: SMI, Net Disposable Margin, Sleep
 · Domain: Capital Efficiency & Transaction Velocity · Domain: Neural Safety Cues & Replacement
 · Levers: Monetary Easing, Subsidies, Corp Cuts     · Levers: Direct Excision of Fixed Overhead
```

### 1.2 Mandatory Operational Runtime Preconditions
The mathematical models in this repository operate exclusively within environments satisfying three structural preconditions:
1. **Monetized Market Economy:** Critical survival overhead is settled in fiat currency via competitive markets (excluding unpriced subsistence agrarian barters or command rationing).
2. **Individual Autonomy & Free Will:** Individuals possess statutory and legal autonomy over marriage, reproduction, and lifestyle (excluding institutional coercion or forced reproduction).
3. **Offspring as Net Economic Liabilities ($P_{net} < 1.0$):** Mandatory education and child labor bans ensure dependent children represent a unidirectional fixed overhead for 18–22 years.

---

## 2. Layer 1 Base Dimensionless Equation (SMI Lite Standard)

For any discrete spatial mesh or cohort $i$ at time $t$, the **Social Margin Index (SMI)** is defined as:

$$SMI_{i, t} = \frac{WCI_{i, t}}{C_{surv\_std}(i, t)}$$

* **$SMI_{i, t} \in \mathbb{R}^+$**: Dimensionless scalar multiplier independent of currency unit or nominal inflation.
* **$WCI_{i, t}$ (Working Capital Income)**: Median real disposable take-home pay of prime young singles (ages 25–34), net of income taxes and mandatory social contributions.
* **$C_{surv\_std}(i, t)$ (Standard Survival Cost)**: Unavoidable baseline fixed overhead required to maintain continuous economic participation and baseline reproductive solvency:

$$C_{surv\_std} = C_{base} + C_{semi}$$

$$C_{base} = C_{rent} + C_{food\_min} + C_{infra\_vital}$$

$$C_{semi} = C_{tax\_ins} + C_{depr} + C_{conn} + (\theta \cdot R_{rel})$$

---

## 3. The Four Phase Transition Thresholds

The SMI metric categorizes demographic states into four distinct operational modes:

```text
   SMI Value        System Dynamic Mode            Operational State & Empirical Expression
───────────────────────────────────────────────────────────────────────────────────────────────
   < 0.60           Mode 0: Autonomic Shutdown     Prefrontal Bandwidth Exhaustion (Chronic Deficit)
                                                   Extreme reproductive lockout; TFR crashes to 0.6–0.9.
                                                   Young adults consume future health/capital to survive.
───────────────────────────────────────────────────────────────────────────────────────────────
   1.00             Mode 1: Break-even Subsistence Zero-Buffer Single Solvency Line
                                                   Bare self-sustenance; zero capacity for dependent life.
                                                   Marriage ceases; pair-bonding triggers systemic panic.
───────────────────────────────────────────────────────────────────────────────────────────────
   1.40             Mode 2: Goldilocks Zone        Biological Pair-Bonding & Household Formation Buffer
                                                   Matches OECD equivalence scale (+40% surplus headroom).
                                                   Cognitive defensive brake releases; spontaneous marriage.
───────────────────────────────────────────────────────────────────────────────────────────────
   ≥ 2.07           Mode 3: Expansion Vector       Demographic Replacement & Capital Surplus
                                                   Stable self-sustaining fertility ($TFR \ge 2.10$).
                                                   Generational succession secured without external input.
───────────────────────────────────────────────────────────────────────────────────────────────
```

---

## 4. Transfer Function & The 4-Year Biological Lag

The empirical response of total fertility (TFR) to changes in SMI follows a **4-Parameter Logistic (4PL) Sigmoid Function** coupled with a **finite distributed lag impulse response ($\approx 4\text{ years}$)**:

$$TFR(SMI) = TFR_{min} + \frac{TFR_{max} - TFR_{min}}{1 + \left(\frac{SMI}{SMI_0}\right)^{-k}}$$

$$TFR_t = \sum_{\tau=3}^{5} w_\tau \cdot TFR\Big(SMI(t - \tau)\Big), \quad \mathbf{w} = \begin{bmatrix} 0.20 \\ 0.65 \\ 0.15 \end{bmatrix}$$

```text
t = 0 Years    t + 1 Year     t + 2 Years    t + 3 Years    t + 4 Years (Empirical Peak)
───┼──────────────┼──────────────┼──────────────┼──────────────┼──────────────▶
 [SMI Recovery]  [Neural Defrost] [Mate Search]  [Pair-Bonding] [First Birth / TFR Spike]
 (Intervention)  (Cortisol Drops)(Infrastructure)(Consolidation)(Macroeconomic Data)
```

Across large K-strategy mammals, gestation and courtship scale as an invariant proportion ($\approx 5\%$) of adult lifespan. In humans ($70\text{--}80\text{ year adult horizon}$), $5\%$ equates to $3.5\text{--}4.0\text{ years}$. Interventions on fixed overhead today take four years to register in headline birth statistics.

---

## 5. Domain-Specific Navigation (Academic Gateways)

This repository provides rigorous specifications tailored across academic and engineering disciplines:

* 📊 **For Econometricians & Demographers:**  
  $\to$ [docs/SPECIFICATION_LITE.md](./docs/SPECIFICATION_LITE.md)  
  *Detailed mathematical derivations, quasi-fixed cost algebra, and distributed lag econometric formulations.*
* 🧬 **For Evolutionary Biologists & Ecologists:**  
  $\to$ [docs/PHILOSOPHY_AND_DYNAMICS.md](./docs/PHILOSOPHY_AND_DYNAMICS.md)  
  *Charnov life-history invariants, mammalian metabolic allocation trade-offs, and limits of external labor arbitrage.*
* 🧠 **For Neuroscientists, Physiologists & Public Health Epidemiologists:**  
  $\to$ [`docs/en/PHILOSOPHY_AND_DYNAMICS.md`](./docs/en/PHILOSOPHY_AND_DYNAMICS.md)  
  Scarcity bandwidth requisition, prefrontal executive fatigue, and the tripartite coupling of HPA-axis activation: reproductive shutdown, metabolic hoarding (BMI escalation), and sleep architecture collapse.
* 🛠️ **For Data Scientists & Quantitative Modelers:**  
  $\to$ [docs/BENCHMARK_AND_ISSUES.md](./docs/BENCHMARK_AND_ISSUES.md)  
  *Public benchmark datasets (e-Stat, CPS, OECD), falsifiability criteria, and the 11 Open Technical Issues.*

---

## 6. Input/Output Data Schema (JSON Schema v7 Reference)

Standardized JSON schema for automated ETL pipelines and municipal diagnostic engines:

```json
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

---

## 7. Structural Extension: Layer 2 Core Protocol (Classified / Restricted)

While this public repository formalizes **Layer 1 (individual bioenergetic margins and standard TFR response)**, real-world sovereign survival is also governed by localized spatial clustering, non-linear civic friction, and demographic succession timelines.

We maintain a restricted second tier: **SMI Core Protocol (State OS Layer 2)**.

```text
       ┌─────────────────────────────────────────────────────────────┐
       │   【Global Common Layer: Open Protocol (SMI Engine)】       │
       │     - SMI Base Equation (Dimensionless Energy Ratio)        │
       │     - 4PL Sigmoid Response & 5% Lifespan Dynamic Lag (t+4)  │
       │     - Standard Data Schema (SMI-OpenAPI / JSON Schema)      │
       └──────────────────────────────┬──────────────────────────────┘
                                      │
              ┌───────────────────────┴───────────────────────┐
              ▼                                               ▼
┌───────────────────────────┐                   ┌───────────────────────────┐
│  【Nation A: Custom OS】  │                   │  【Nation B: Custom OS】  │
│ · Raw Data (On-Premises)  │                   │ · Raw Data (On-Premises)  │
│ · Sovereign Plugins       │                   │ · Sovereign Plugins       │
│   (Housing, Taxes, Family)│                   │   (Student Debt, Private) │
│ · Fully Air-Gapped/Secret │                   │ · Fully Air-Gapped/Secret │
└─────────────┬─────────────┘                   └─────────────┬─────────────┘
              │                                               │
              └───────────────────────┬───────────────────────┘
                                      ▼
       ┌─────────────────────────────────────────────────────────────┐
       │      【Allied Federated Knowledge Network (Zero Raw Data)】 │
       │  Raw administrative telemetry is 100% air-gapped locally.   │
       │  Only anonymized systemic sensitivities are synchronized:   │
       │   1. Policy Elasticities: Overhead Reduction % vs. ΔSMI     │
       │   2. Coordinated Demarcation: Sovereign Failure Deadlines   │
       └─────────────────────────────────────────────────────────────┘
```

### Layer 2 Restricted Engine Features:
* **Non-linear Spatial Friction Function ($\text{Toxicity}$):** Multi-variable sigmoidal expansion calculating marginal overhead explosions driven by local density ($D_{local}$), normative distance ($H_{dist}$), and spatial clustering ($C_{cluster}$).
* **Spatial Phase Separation (Phase 1–3 / PoR):** Mathematical boundary conditions defining irreversible loss of sovereign policing and municipal authority (Point of No Return).
* **The 20-Year Primary Failure Line:** Deterministic generational horizon models projecting defense, police, and critical infrastructure personnel collapses.

#### 🔒 Accessing Layer 2 Core Protocol
Access to `SMI-Framework-Core` is restricted to verified research organs, municipal planners, and sovereign security analysts. Uncontrolled public distribution is restricted to prevent speculative municipal shorting and hostile geopolitical targeting.

* **Repository:** `SMI-Framework-Core` (Private / Vetted Collaborators)
* **Inquiries:** Submit identity verification via repository Security Advisories or official institutional contact.

---

## 8. License & Intellectual Property

* **Layer 1 Specifications (This Repository):** Released under the **[MIT License](./LICENSE)**. Free for academic citation, municipal deployment, and commercial integration.
* **Architecture & Terminology:** All foundational concepts (*SMI*, *WCI*, *Toxicity Phase Transitions*, *State OS Architecture*) remain the intellectual property of the project architect.
