# SMI Framework (Social Margin Index) - v1.0 [Open Standard]

[English](./README.md) | [日本語](./README.ja.md)

> **"The survival or collapse of human civilization is governed not by moral narratives or cultural values, but by the physical laws of disposable survival energy."**

The SMI Framework is an open-source, socioeconomic engineering protocol (State OS Core Architecture) designed to quantify, forecast, and simulate the mechanisms driving ultra-low fertility, marriage market collapse, and structural societal decline in advanced capitalist economies as a thermodynamic energy balance problem[cite: 1, 2, 4].

---

## 1. System Philosophy & Operational Boundary Conditions

### 1.1 Philosophy: Releasing the Autonomic Shutdown
In contemporary post-industrial and urbanized societies, collapsing fertility rates and plunging marriage rates have long been framed through moralistic or qualitative narratives: "the rise of herbivore men," "shifting youth priorities," or "insufficient childcare subsidies"[cite: 1, 2, 4]. However, despite massive deployments of symptomatic welfare transfers and public awareness initiatives, the downward trajectory of aggregate reproductive dynamics remains unbroken[cite: 1, 4].

*Homo sapiens*, as large mammals operating under an evolutionary K-strategy, possess hardwired homeostatic defenses[cite: 1, 2, 4]. When an individual's baseline survival margin is severely eroded, the prefrontal cortex and hypothalamic-pituitary-adrenal (HPA) axis execute an **Autonomic Shutdown**—a biological failsafe that actively cuts off long-term investments, romantic coupling, and reproductive behavior[cite: 1, 2, 4].

This protocol does not advocate political dogma, moral prescriptions, or ideological doctrines[cite: 4]. Instead, it introduces a **dimensionless physical metric (Vital Monitor)** into socioeconomic systems, establishing a universal diagnostic specification for state, municipal, and institutional architectures[cite: 1, 2, 4].

### 1.2 Mandatory Operational Boundary Conditions
This model is not an unconstrained, universal abstraction applicable to all historic or tribal ecosystems. It is a deterministic physical model calibrated exclusively for modern urban capitalist social systems that satisfy the following three operational preconditions[cite: 1, 7]:

1. **Monetized Market Economy:** The overwhelming majority of baseline survival, housing, and reproductive costs are procured through competitive markets and settled in fiat currency (excluding pure subsistence barter economies or unpriced command ration systems)[cite: 1, 7].
2. **Individual Autonomy & Reproductive Choice:** Individuals possess full legal, statutory, and cultural rights over marriage, singlehood, contraception, and personal lifestyle choices (excluding slave-based economies or closed patriarchal communities enforced by religious dogma)[cite: 1, 7].
3. **Offspring as Structural Net Economic Liabilities ($P_{net} < 1.0$):** Under child-labor bans and compulsory education, dependent children represent a structural net financial liability for 18–22 years, unable to contribute labor or income to parental cash flow (excluding traditional agrarian societies where child labor yields net positive returns)[cite: 1, 2, 7].

---

## 2. Core Mathematical Specification (Layer 1: SMI Lite)

The ratio between the disposable energy an individual (young single cohort) can capture and the non-negotiable metabolic maintenance costs imposed by society is defined as the **SMI (Social Margin Index)**[cite: 1, 4]:

$$SMI = \frac{WCI}{C_{surv\_std}} = \frac{WCI}{C_{base} + C_{semi}}$$

### Variable Definitions

* **$WCI$ (Working Capital Income)**  
  The median real disposable income (net take-home pay after statutory taxes and mandatory social security contributions) of prime young singles (ages 25–34) within a defined target region[cite: 1, 2, 7].
* **$C_{surv\_std}$ (Standard Survival Cost)**  
  The baseline fixed cost required to maintain independent, healthy participation in society—distinct from minimum welfare or poverty-line thresholds[cite: 1, 2].
  $$C_{base} = C_{rent} + C_{food\_min} + C_{infra\_vital}$$
  $$C_{semi} = C_{tax\_ins} + C_{depr} + C_{conn} + (\theta \cdot R_{rel})$$
  * $C_{rent}$: Median private market rent for standard 25–30 sqm single-occupancy units[cite: 1, 2]
  * $C_{food\_min}$: Baseline nutritional expenditures ensuring essential metabolic balances
  * $C_{infra\_vital}$: Lifeline utility expenditures (electricity, gas, water)[cite: 4]
  * $C_{tax\_ins}$: Marginal statutory drag (payroll taxes, health levies, and mandatory pension deductions)[cite: 1, 2]
  * $C_{depr}$: Amortized sinking fund for domestic appliance depreciation, lease renewal fees, preventive health, and contingency reserves[cite: 1, 2]
  * $C_{conn}$: Non-discretionary modern digital connectivity (broadband and mobile infrastructure)
  * $\theta \cdot R_{rel}$: Relative positional drag (status-driven educational competition and peer-group signaling overhead)[cite: 4, 8]

> **Methodological Exclusion of Headline CPI:**  
> The denominator ($C_{surv\_std}$) deliberately rejects deflators based on aggregate Consumer Price Indices (Headline CPI)[cite: 1, 2]. Headline CPI metrics are diluted by technological deflation in consumer durables and non-essential goods[cite: 8]. SMI measures only the raw physical basket of **unavoidable existential fixed costs** directly sensed by the organism's survival hardware[cite: 1, 2, 8].

---

## 3. The 4 Phase Transition Thresholds

Because the SMI operates as a dimensionless ratio (pure scalar multiple) that normalizes local currencies and inflation, its phase thresholds represent universal biological boundaries across borders, regimes, and eras[cite: 1, 2].

| SMI Metric | System State | Biological & Social Dynamics |
| :--- | :--- | :--- |
| **$SMI < 0.60$** | **Autonomic Shutdown (Self-Cannibalization Zone)** | Maintaining single survival requires liquidating future depreciation buffers. The neural circuitry engages an emergency brake, biologically disabling long-term investments, marriage, and reproduction (current status of East Asian metropolitan centers)[cite: 1, 2, 4]. |
| **$1.00 \le SMI < 1.40$** | **Payload-Zero Baseline (Defensive Margin)** | Individual self-sufficiency is maintained, but excess metabolic buffer is zero. Individuals lack the operational margin to support another life, locking the system into demographic stagnation[cite: 1, 2, 4]. |
| **$1.40 \le SMI < 2.07$** | **Reproductive Goldilocks Zone** | A stable surplus margin exceeding baseline maintenance by $\ge 40\%$ is maintained. This mathematically aligns with the OECD equivalence scale ($+0.4$ incremental household formation scale), enabling natural recovery toward replacement levels (TFR 2.07)[cite: 1, 2, 4]. |
| **$SMI \ge 2.07$** | **Emergency Impulse Boost** | A transient high-voltage recharge regime (3–5 year time-locked intervention) designed to break deep multi-decade neural shutdown and unfreeze collective reproductive capacity[cite: 1, 2, 4]. |

---

## 4. Transfer Function & Temporal Dynamics

### 1) Non-linear TFR Response (4-Parameter Logistic Equation)
The response of total fertility (TFR) to SMI improvements does not follow a linear path; it forms an S-shaped sigmoid curve with an asymptotic carrying-capacity ceiling ($TFR_{max}$)[cite: 1, 2]:

$$TFR(SMI) = TFR_{min} + \frac{TFR_{max} - TFR_{min}}{1 + \left(\frac{SMI}{SMI_0}\right)^{-k}}$$

* $SMI_0 \approx 1.05$ (Inflection Point: threshold where systemic reproductive release begins)[cite: 2, 7]
* $k \approx 4.0$ (Hill-equivalent slope sensitivity parameter)[cite: 2, 7]
* $TFR_{min} \approx 0.65$ (Biological floor under extreme economic compression)[cite: 2, 8]
* $TFR_{max} \approx 2.15$ (Asymptotic social carrying capacity under modern urban constraints)[cite: 2, 4]

### 2) Distributed Lag Model (5% Life-Span Constant)
Derived from K-strategy life-history constraints, the systemic lag between environmental improvement (rising SMI) and maternal realization (rising TFR) operates over approximately 5% of adult life expectancy—manifesting as a 3-to-5-year distributed lag (peaking at $t+4$ years)[cite: 1, 2, 4]:

$$TFR_t = \sum_{\tau=3}^{5} w_\tau \cdot 4PL(SMI_{t-\tau}) \quad (w_3 = 0.20, \ w_4 = 0.65, \ w_5 = 0.15)$$[cite: 1, 2]

---

## 5. Input/Output Data Schema (JSON Schema v7)

Data exchange with the SMI analytical engine must conform to the following schema definition[cite: 1, 2]:

```json
{
  "$schema": "[http://json-schema.org/draft-07/schema#](http://json-schema.org/draft-07/schema#)",
  "title": "SMIEvaluationInput",
  "type": "object",
  "required": ["country_iso", "mesh_id", "year", "economic_inputs", "survival_costs"],
  "properties": {
    "country_iso": { "type": "string", "pattern": "^[A-Z]{3}$" },
    "mesh_id": { "type": "string" },
    "year": { "type": "integer", "minimum": 1950, "maximum": 2100 },
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
    "survival_costs": {
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
    }
  }
}

```

---

## 6. Academic Gateways

Researchers across specialized disciplines can navigate directly to their corresponding domain protocols:

* 📊 **For Econometricians & Demographers:**  
  $\to$ [`docs/en/SPECIFICATION_LITE.md`](./docs/en/SPECIFICATION_LITE.md)  
  Automated mapping pipelines for official statistics (SNA, US Census/CPS, OECD Family Database) and distributed lag regression specifications.
* 🧬 **For Evolutionary Biologists & Ecologists:**  
  $\to$ [`docs/en/PHILOSOPHY_AND_DYNAMICS.md`](./docs/en/PHILOSOPHY_AND_DYNAMICS.md)  
  Integration with Life History Theory, Charnov dimensionless invariants, and the 5% adult lifespan reproductive gestation lag[cite: 1, 2, 8].
* 🧠 **For Neuroscientists & Behavioral Economists:**  
  $\to$ [`docs/en/PHILOSOPHY_AND_DYNAMICS.md`](./docs/en/PHILOSOPHY_AND_DYNAMICS.md)  
  Scarcity bandwidth requisition, prefrontal cortex executive fatigue, and HPA-axis mediated autonomic mating cessation[cite: 1, 2, 8].
* 📐 **For Complex Systems Theorists & Physicists:**  
  $\to$ [`docs/en/SPECIFICATION_LITE.md`](./docs/en/SPECIFICATION_LITE.md)  
  4PL sigmoid properties, non-linear saturation parameters, and phase transition mechanics.
* 🛠️ **For Contributors & Red-Teamers:**  
  $\to$ [`docs/en/BENCHMARK_AND_ISSUES.md`](./docs/en/BENCHMARK_AND_ISSUES.md)  
  The 14-item open issue master list, falsifiability boundaries, and standard benchmark datasets.

---

## 7. Structural Extension: Layer 2 Core Kernel Protocol

The baseline model provided in this public repository (Layer 1) operates as an open standard tracking individual thermodynamic energy surplus and reproductive viability[cite: 1, 15].

However, macroscopic sovereign survival is constrained by additional endogenous variables:  
**"Spatial Density," "Normative/Cultural Distance," and "Non-linear Social Friction (Toxicity)"**,  
which trigger regional phase separation (Parallel Societies / Autonomous Enclaves)[cite: 1, 15].

The SMI Framework integrates these dynamics into an institutional-grade **Layer 2 Core Kernel**[cite: 1, 15]:

* Closed-form non-linear spatial friction equations ($\text{Toxicity}$)
* Spatial phase separation algorithms (Phase 1–3 / Point of No Return)
* 20-Year Primary Sovereign Failure Line trajectory projections

---

### 🔒 Layer 2 Core Specifications & R&D Access Request

To protect sovereign stability and prevent ideological noise, the complete specification (`SPECIFICATION_CORE.md`) and private R&D issue trackers are quarantined within private repositories[cite: 11, 15].  
Access is granted exclusively to vetted institutional analysts, academic researchers, defense organs, and qualified systems architects[cite: 11, 15].

To request vetted access, submit your verification credentials via the official portal[cite: 11, 15]:

👉 **[Layer 2 Core Protocol Vetting & Access Portal](https://forms.gle/tHVG5mxRhNGaQpfeA)**  
*(※ Please note that administrative review and invitation issuance may take some lead time due to independent governance)*
> 
> 

---

## 8. Technical Discussions & Call for Pull Requests

This protocol prioritizes architectural conceptualization and formal systems modeling[cite: 7, 8].

We welcome empirical econometric backtests (using Census, Household Budget, and OECD series), mathematical parameter calibrations, and simulation implementations via GitHub Discussions and Pull Requests[cite: 7, 8]:

* **Model & Math Calibration:** Formal proposals for parameter tuning and transfer functions.
* **Data Pipelines & Normalization:** Automated extraction scripts (e-Stat, OECD, CPS) and cross-national schema mapping.
* **Biological & Cognitive Mechanisms:** Empirical citations and clinical literature cross-referencing.

---

## 9. License

* **Layer 1 Open Standard (SMI Base):** [MIT License](./LICENSE)  
  Academic usage, citations, quantitative research, and private commercial integration are unrestricted.
* **Layer 2 Kernel (State OS Core):** All Rights Reserved (Restricted Institutional Access).
