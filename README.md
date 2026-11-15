# SMI Framework (Social Margin Index)

[English](./README.md) | [日本語](./README.ja.md)

> **"Societal survival and demographic fertility are governed not by moralizing narratives or cultural 'poetry,' but deterministically by real disposable metabolic energy ratios (a dimensionless scalar) remaining after unavoidable fixed overhead is deducted."**

The **SMI Framework** is an open-source sociophysical and econometric protocol that quantifies individual disposable survival margins in modern urban capitalist societies to forecast long-term Total Fertility Rate (TFR) trajectories and systemic phase transitions.

## 1. Operational Runtime Preconditions & Dual-Aspect Economics

This framework is not an unconstrained universal abstraction applicable to all historical eras or tribal ecosystems. It is a deterministic physical model calibrated exclusively for social systems satisfying three structural runtime conditions (**The Modern Urban-Capitalist OS**):

1. **Monetized Market Economy:** Primary survival and reproductive overheads (housing, nutrition, vital utilities, education, taxation, and social security) are settled predominantly via fiat currency in competitive markets (excluding subsistence agrarian communes or universal state rationing).
2. **Individual Autonomy & Free Will:** Both sexes possess legally and institutionally guaranteed autonomy regarding marriage, non-marriage, contraception, and lifestyle choices (excluding forced marital institutions or coercive enclaves).
3. **Structural Child Net Cost ($P_{net} < 1.0$):** Child labor prohibitions and compulsory schooling ensure dependent offspring represent unidirectional fixed economic liabilities until adulthood (excluding pre-industrial agrarian systems where child labor yields net household surpluses).

### 1.1 Decoupling Industrial Throughput from Biological Margin

Conventional macroeconomics conflates two distinct thermodynamic states under the single label of "economic conditions":

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

SMI does not invalidate Channel A industrial policy; rather, it retrofits the missing **Channel B vital gauge** required to prevent biological engine seizure (demographic and domestic demand collapse).

## 2. Core Equation & Dual-Lens Observation Architecture

### 2.1 Base Dimensionless Equation (SMI Lite Standard)

For a given spatial mesh or demographic cohort $i$ at time $t$, the **Social Margin Index (SMI)** is defined as a dimensionless scalar ratio independent of currency units or nominal inflation:

$$
SMI_{i, t} = \frac{WCI_{i, t}}{C_{surv\_std}(i, t)}
$$

* **Numerator** $WCI_{i, t}$ **(Working Capital Income):** Median real net disposable income of young single adults (ages 25–34) after income taxes, local taxes, and mandatory social security deductions.
* **Denominator** $C_{surv\_std}(i, t)$ **(Standard Survival Cost):** Linear sum of absolute fixed costs (median private market rent, baseline nutrition, vital utilities) and quasi-fixed social survival costs (marginal tax/insurance wedge, depreciation reserves, essential telecom, and relative conformity/educational overhead $\theta \cdot R_{rel}$).
  * *Note: Official headline CPI deflation is intentionally excluded, as hedonic price drops in consumer electronics severely distort real biological survival inflation.*

### 2.2 Dual-Lens Observation (Standard Lens & Canary Model)

Without altering the core equation ("the camera body"), the SMI Framework switches input income quantile filters ("the optical lenses") to achieve both macro fertility forecasting and early-warning detection of structural decay:

* **Standard Lens (Population Median $P50$):** Evaluates median young single adults (ages 25–34) within the self-supporting labor market (Track A). Passed through a **3–5 year distributed lag (peaking at 4 years)** and a 4PL logistic transfer function, it forecasts national and regional TFR trajectories.
* **Canary Lens (Lower-Tier Working Cohort $Q25\text{–}Q40$):** Evaluates lower-tier regular and non-regular formal workers (Track A) using the identical formula. Operating with zero asset buffers, this cohort breaches the $0.60$ shutdown threshold and compresses against the physical floor **12 to 15 years prior** to median middle-class collapse, serving as an early-warning indicator.

## 3. Five Universal Phase Transition Thresholds

The dimensionless scalar $SMI$ mechanically classifies bio-social states across five universal phase thresholds, invariant across nations and cultures:

| SMI Range / Threshold | Regime Status | Physical & Bio-Social System State |
| :--- | :--- | :--- |
| $\ge 2.07$ | **Replacement Boost Zone** | Total Fertility Rate stably exceeds replacement ($\approx 2.07$), driving organic population growth. |
| $1.40$ | **Household Formation Golden Zone** | Equilibrium cruising altitude aligned with OECD equivalence scales ($+0.5$ additional adult, $+0.3$ per child). |
| $1.00$ | **Unloaded Break-Even Line** | Single individual barely achieves cash-flow equilibrium inclusive of depreciation reserves (zero shock buffer). |
| $< 0.60$ | **Autonomic Shutdown / Cannibalization** | Prefrontal executive defense brakes engage; individuals liquidate future health/depreciation reserves while ceasing reproduction. |
| $\approx 0.45$ | **Labor Market Floor Constant** | Empirical physical lower bound ($0.44 \sim 0.53$) observed across structurally divergent advanced economies (Japan, US, Sweden, Italy, Hungary) for populations remaining in self-supporting formal labor (Track A). Compression below this floor triggers forced phase transition into public assistance dependency (Track B) or underground/high-friction instability ($\text{Toxicity}$). |

## 4. Empirical Benchmarks & Cross-National Highlights

* **Post-War to Modern Japan Backtest:** Calibrated strictly on pre-1990 structural data, the SMI transfer curve predicts the subsequent 30-year fertility decline ($1991\text{–}2020$) with an out-of-sample $R^2 > 0.81$ (peaking at a 4-year biological lag).
* **Cross-National 4-Country Validation (US, Sweden, Italy, Hungary):** Across four advanced nations with diametrically opposed tax, welfare, and family-allowance architectures, the Track A Canary cohort ($Q25\text{–}Q40$) converges consistently onto the **$0.44 \sim 0.53$ Labor Market Floor**. Furthermore, the timing of Canary breaches below $0.60$ aligns chronologically with macro surges in social friction, public order degradation, and systemic polarization.

## 5. Documentation Map

This public repository (**Layer 1: Open Standard**) consists of the following core specifications:

* [**`docs/SPECIFICATION_LITE.md`**](./docs/SPECIFICATION_LITE.md) ([日本語](./docs/SPECIFICATION_LITE.ja.md))
  Layer 1 Mathematical Specification. Defines denominator decomposition, Dual-Lens observation (Standard / Canary), 4PL sigmoid response, 3–5 year FIR distributed lag, Track A/B separation rules, and JSON Schema v1.1.
* [**`docs/PHILOSOPHY_AND_DYNAMICS.md`**](./docs/PHILOSOPHY_AND_DYNAMICS.md) ([日本語](./docs/PHILOSOPHY_AND_DYNAMICS.ja.md))
  Theoretical Foundations & Bio-Dynamics. Formalizes dual-aspect economics, Charnov life-history invariants (5% adult lifespan lag), prefrontal cognitive bandwidth requisition, HPA-axis shutdown/metabolic hoarding/sleep collapse, and the thermodynamic limits of labor importation.
* [**`docs/BENCHMARK_AND_ISSUES.md`**](./docs/BENCHMARK_AND_ISSUES.md) ([日本語](./docs/BENCHMARK_AND_ISSUES.ja.md))
  Empirical Benchmarks & Open Issues Master. Defines strict falsifiability boundaries (null hypotheses), Japanese/US/OECD/4-nation validation pipelines, and the domain-sorted open technical issues.

## 6. Academic Gateways

Researchers and practitioners can navigate directly to the protocols matching their analytical toolkits:

* 📊 **For Econometricians & Demographers:**
  $\to$ [`docs/SPECIFICATION_LITE.md`](./docs/SPECIFICATION_LITE.md)
  Track A/B separated ETL extraction pipelines (e-Stat, US CPS, OECD.Stat) and FIR distributed lag regression specifications.
* 🧬 **For Evolutionary Biologists & Behavioral Ecologists:**
  $\to$ [`docs/PHILOSOPHY_AND_DYNAMICS.md`](./docs/PHILOSOPHY_AND_DYNAMICS.md)
  Life-history theory for K-selected large mammals, Charnov dimensionless invariants, and the 5% adult lifespan (~4-year) reproductive gestation lag.
* 🧠 **For Neuroscientists, Physiologists & Public Health Epidemiologists:**
  $\to$ [`docs/PHILOSOPHY_AND_DYNAMICS.md`](./docs/PHILOSOPHY_AND_DYNAMICS.md)
  Scarcity bandwidth requisition in the prefrontal cortex and the tripartite HPA-axis stress coupling: reproductive shutdown, defensive visceral fat hoarding (BMI escalation), and slow-wave sleep collapse.
* 📐 **For Complex Systems Theorists & Statistical Physicists:**
  $\to$ [`docs/SPECIFICATION_LITE.md`](./docs/SPECIFICATION_LITE.md)
  4PL logistic phase-transition characteristics, Canary floor compression dynamics, and non-linear saturation parameters.
* 🛠️ **For Contributors & Red-Teamers:**
  $\to$ [`docs/BENCHMARK_AND_ISSUES.md`](./docs/BENCHMARK_AND_ISSUES.md)
  Explicit model falsification criteria, replication benchmark schemas, and the master open issue list.

## 7. Layer 2 Architecture: The SMI Core Kernel (Security & Spatial Friction Engine)

Layer 1 (**SMI Lite**), hosted publicly in this repository, functions as an open vital monitor tracking individual disposable energy margins and demographic trajectories.

However, macroscopic sovereign and urban stability is governed not merely by isolated household budgets, but by **local spatial density ($D_{local}$)**, **normative institutional/cultural distance ($H_{dist}$)**, and the resulting **non-linear social friction ($\text{Toxicity}$)**—which triggers irreversible spatial phase separation (de facto autonomous enclaves and administrative failure).

The SMI Framework isolates these spatial security and sovereign governance engines within a segregated **Layer 2 Core Kernel**:

* **Non-Linear Friction Function $\text{Toxicity}(t)$:** Models administrative and policing saturation across $1\text{km} \times 1\text{km}$ spatial meshes, coupled with Layer 1 Canary collapse triggers ($SMI_{canary} < 0.60 \to 0.45$).
* **Spatial Phase Separation & Point of No Return (PoR) Detection:** Extends Schelling segregation thresholds to compute mathematical criticalities (Phase 1–3 / PoR) where standard governance fails.
* **20-Year Generational Trajectory & Primary Sovereign Collapse Line:** Forecasts dynamic intersections between second-generation demographic spikes (20 years post-inflow) and acute physical deficits in domestic defense and critical infrastructure personnel.

### 🔒 Layer 2 Core Specifications & Access Vetting

To prevent bad-faith politicization and maintain rigorous engineering discipline, complete Layer 2 specifications (`SPECIFICATION_CORE.md`) and private R&D trackers are quarantined in private repositories. Access is restricted exclusively to vetted research institutions, policy analysts, defense/security organs, and qualified systems architects.

Vetting and access requests are processed via the official portal:

👉 [**Layer 2 Core Protocol Vetting & Access Portal**](https://forms.gle/YourGoogleFormLinkPlaceholder)

*(Note: Independent governance review may require lead time prior to invitation issuance.)*

## 8. Technical Discussions & Call for Pull Requests

This protocol prioritizes formal architectural design and empirical falsifiability. We welcome Pull Requests and technical discussions covering econometric backtests, parameter calibrations, and simulation implementations:

* **Model & Math Calibration:** Parameter tuning and transfer function refinements.
* **Data Pipelines & Normalization:** Automated Track A/B separation scripts (e-Stat, CPS, Eurostat, OECD) and schema mapping.
* **Biological & Cognitive Mechanisms:** Clinical literature cross-referencing and neuroendocrine validation.

## 9. License

* **Layer 1 Open Standard (SMI Base Standard):** [MIT License](./LICENSE)
  Academic usage, citation, quantitative research, and commercial integration are unrestricted.
* **Layer 2 Kernel (State OS Core Kernel):** All Rights Reserved (Restricted Institutional Access).
