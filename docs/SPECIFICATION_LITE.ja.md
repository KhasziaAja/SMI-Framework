# SMI Framework: Layer 1 数理仕様書 (SPECIFICATION_LITE) - v1.0

[English](../en/SPECIFICATION_LITE.md) | [日本語](./SPECIFICATION_LITE.ja.md)

> **"個体の行動選択は主観的効用ではなく、不可避な固定費を差し引いた後の実効エネルギー残量（無次元比率）によって拘束される。"**

---

## 1. 動作環境と適用境界条件（Operational Preconditions & Boundary Conditions）

本数理モデルは、無条件にあらゆる社会・生態系で動作する汎用抽象論ではなく、特定の社会OS（経済・法的基盤）の上でのみ機能する決定論的物理モデルである[cite: 1, 5]。モデルの健全な動作および科学的妥当性を担保するため、以下の3大適用境界条件を前提動作環境（Runtime Environment）として規定する[cite: 1, 5]。

### 1.1 前提条件1：貨幣・市場決済経済（Monetized Market Economy）
個体の生存・再生産に必要な主要固定費（住居、食糧、光熱インフラ、教育、税・社会保障）の大半が市場を介し、**「法定通貨」**によって決済されている社会構造であること[cite: 1, 5]。
* **適用除外（Out of Scope）：** 完全自給自足の伝統的農村共同体、あるいは住居・医療・食糧が無償配給された旧ソ連型共産主義体制[cite: 1, 5]。これらの社会では市場価格としての「分母」が存在しないか著しく歪曲されるため、本モデルの直接評価対象外とする[cite: 1, 5]。

### 1.2 前提条件2：個体の自由意志と契約自律性（Individual Autonomy & Free Will）
個体（男女）に「未婚・不婚・避妊・生活様式の選択」という**自律的意思決定権**が法的・制度的に担保されていること[cite: 1, 5]。
* **適用除外（Out of Scope）：** 奴隷制、強制配偶制度、あるいは宗教的ドグマや家父長制によって生殖が強制される閉鎖的共同体[cite: 1, 5]。これらの環境では前頭前野の生存防衛ブレーキが物理的・強制的に無効化され、「人間モデル（SMI）」から「家畜管理・農学モデル」へ相転移するため本仕様の対象外となる[cite: 1, 5]。

### 1.3 前提条件3：子どもの構造的純負債化（Child Net Cost / $P_{net} < 1.0$）
児童労働の禁止、義務教育の普及、および近代都市労働環境により、子どもが成人（18〜22歳）に達するまで一方的な消費主体（固定費・純負債）であり、親の直接的な労働力・家計の収益源になり得ない近代都市型社会であること[cite: 1, 2, 5]。
* **適用除外（Out of Scope）：** 子どもが5歳前後から農業労働力や家事労働として分子（家計所得）に寄与し、「産むほど家計が黒字化する（$P_{net} > 1.0$）」前近代的な伝統農村社会[cite: 1, 2, 5]。

---

## 2. 基礎方程式と変数の工学的定義

本章では、上記前提条件を満たす近代都市資本主義社会における第1階層（SMI Lite Standard）の数理モデル、変数型、伝達関数、および正規化プロトコルを定義する[cite: 1, 2]。

### 2.1 基礎方程式（Base Dimensionless Equation）

対象空間メッシュまたは集団 $i$ の時点 $t$ における **SMI (Social Margin Index)** を以下のように定義する[cite: 1, 2]。

$$SMI_{i, t} = \frac{WCI_{i, t}}{C_{surv\_std}(i, t)}$$

* **出力 $SMI_{i, t} \in \mathbb{R}^+$**: 通貨単位や名目インフレに依存しない無次元スカラー量（倍率）[cite: 1, 2]。
* **分子 $WCI_{i, t}$ (Working Capital Income)**: 若年単身層（25〜34歳）の実効可処分所得中央値（所得税・住民税・社会保険料控除後手取り）[cite: 1, 2, 5]。
* **分母 $C_{surv\_std}(i, t)$ (Standard Survival Cost)**: 健全な社会参加と再生産可能性を維持するための標準生存固定費[cite: 1, 2]。

---

### 2.2 分母 $C_{surv\_std}$ の解剖：絶対固定費と「準固定費」の境界

公的扶助基準（最低生活費）や純粋な生理的限界費用のみを分母に算入した場合、$WCI \approx 20\text{万円}$ に対し生活費が約 $14\text{〜}15\text{万円}$ となり、$SMI \approx 1.3\text{〜}1.4$ が算出される[cite: 1, 2, 5]。この場合、表見上は「自立可能で健全」に見えるにもかかわらず、実際には未婚化・少子化が極限まで加速するという深刻な統計的乖離（欺瞞）が発生する[cite: 1, 2, 5]。

この乖離を解消するため、本モデルでは分母を**「絶対固定費（生体維持費）」**と**「準固定費（社会存続・防衛費）」**の厳密な線形結合として定義する[cite: 1, 2]。

$$C_{surv\_std} = C_{base} + C_{semi}$$

$$C_{base} = C_{rent} + C_{food\_min} + C_{infra\_vital}$$

$$C_{semi} = C_{tax\_ins} + C_{depr} + C_{conn} + (\theta \cdot R_{rel})$$

> **【公的CPI（消費者物価指数）による実質化の意図的排除】**  
> 本モデルにおける分母（$C_{surv\_std}$）は、公的総合CPIによるデフレートを意図的に排除している[cite: 4]。公的CPIは耐久消費財（テレビ・PC等）の技術革新による価格下落によって生活実感と激しく乖離するため、生体OSが直接感知する**「不可避4大固定費（都市適正家賃・税社保限界負担・必須インフラ・予防医療教育引当）」に限定した実物バスケット（生体生存固定費）**として直接算定・評価する[cite: 4]。

#### 各構成要素の定義とデータ型

| 変数記号 | 項目名称 | 定義・算入基準 | 主な統計ソース（日・米・OECD） |
| :--- | :--- | :--- | :--- |
| $C_{rent}$ | 民間適正家賃 | 単身者向け適正居住面積水準（25〜30㎡）の民間家賃中央値（公的住宅除く）[cite: 1, 2] | 家計調査、民間ポータルAPI、HUD FMR[cite: 2] |
| $C_{food\_min}$ | 基礎栄養維持費 | 生体維持に必要な最低カロリー・PFCバランスを満たす自炊基準費用 | 家計調査（食料費基礎支出） |
| $C_{infra\_vital}$| 必須インフラ費 | 電気・水道・ガス等の生存不可避光熱費[cite: 5] | 家計調査（光熱・水道）[cite: 5] |
| $C_{tax\_ins}$ | 限界公的負担 | 所得から天引きされる住民税、所得税、厚生年金、健康保険等の法定控除[cite: 1, 2] | 国税庁・社保庁基準表、CPS[cite: 2] |
| $C_{depr}$ | 自衛減価償却引当 | 家電更新、敷金礼金・更新料、冠婚葬祭、予防医療等に対する月割引当金[cite: 1, 2] | 総務省「全国単身世帯収支実態調査」 |
| $C_{conn}$ | 就業通信インフラ | 就業および社会活動維持に不可欠なデータ通信回線・スマートフォン端末賦払金 | 通信費実測中央値 |
| $\theta \cdot R_{rel}$| 相対的標準コスト項 | 局所コミュニティで排除・孤立を避けるために要求される世間体・教育競争固定費[cite: 3, 4] | 文部科学省学習費調査、ジニ係数[cite: 4] |

> **【数理的証明：なぜ準固定費でSMIが垂直落下するのか】**  
> 月手取り $WCI = 200,000\text{円}$ に対し、  
> * 絶対固定費のみ：$C_{base} = 65,000(\text{家賃}) + 35,000(\text{食}) + 12,000(\text{光熱}) = 112,000\text{円}$  
>   $$\to SMI_{base} = \frac{200,000}{112,000} \approx 1.78 \quad \text{（健全・再生産可能に見える錯覚）}$$[cite: 1, 2]
> * 準固定費の算入：$C_{semi} = 45,000(\text{社保税実効}) + 20,000(\text{更新・引当}) + 10,000(\text{通信}) + 25,000(\text{世間体・予防医療}) = 100,000\text{円}$[cite: 1, 2]  
>   $$C_{surv\_std} = 112,000 + 100,000 = 212,000\text{円}$$  
>   $$\to SMI = \frac{200,000}{212,000} \approx 0.94 \quad \text{（空荷自立限界線を下回り、自律停止圏へ転落）}$$[cite: 1, 2]  
>
> 準固定費を無視した公的統計は、個体が日常的に払わされている「見えない出血（将来資産の食いつぶし）」を観測できない[cite: 1, 2]。

---

### 2.3 相対的標準コスト項（$R_{rel}$）の定式化

先進国における少子化の本質は、絶対的貧困ではなく「周囲との比較による標準コストのインフレ」である[cite: 3, 4]。これを以下のプラグイン関数としてモデル化する[cite: 3, 4]。

$$R_{rel} = \frac{Median(Edu_{local}) + Gini_{region} \cdot C_{base}}{C_{base}}$$

* $Median(Edu_{local})$: 当該地域メッシュにおける民間塾・習い事・私的教育費の中央値[cite: 4]。
* $Gini_{region}$: 局所の所得格差を示すジニ係数（格差が大きいほど見栄・世間体競争コストが増幅）[cite: 4]。
* $\theta \in [0.0, 1.0]$: 文化・規範感度係数（東アジア圏等、同調圧力が極めて高い地域で $\theta \to 1.0$、個人主義圏で $\theta \to 0.2$）[cite: 3, 4]。

---

### 2.4 共働き世帯における「時間喪失補正モデル」

共働き世帯の世帯合算手取り $I_{household}$ を単純代入すると、育児・家事労働時間の喪失に伴う外部委託コストや認知的摩耗を見落とし、SMIを過大評価する（1.5馬力トラップ）[cite: 1, 2]。  
したがって、世帯評価時の実効 $WCI_{eff}$ は以下の時間減衰関数で補正する[cite: 1, 2]。

$$WCI_{eff} = \frac{WCI_1 + WCI_2}{1 + \lambda \cdot \max\left(0, \frac{H_1 + H_2 - H_{standard}}{H_{standard}}\right)}$$

* $H_1, H_2$: 夫婦それぞれの月間総労働時間（残業・通勤を含む）
* $H_{standard}$: 標準的法定労働時間（例: 160時間/月）
* $\lambda \approx 0.35$: 時間喪失ペナルティ係数（時間的余裕の消滅に伴う外食・民間シッター・精神疲労コストの換算倍率）[cite: 1, 2]

---

## 3. 非線形TFR伝達関数（4PLロジスティック方程式）

SMIの変化に対する合計特殊出生率（TFR）の動態応答は、一次直線ではなく、生体OSの閾値反応および環境収容力による上限飽和を記述する**「4パラメータ・ロジスティック（4PL）シグモイド関数」**によって定式化される[cite: 1, 2]。

### 3.1 伝達関数の完全形

$$TFR(SMI) = TFR_{min} + \frac{TFR_{max} - TFR_{min}}{1 + \left(\frac{SMI}{SMI_0}\right)^{-k}}$$

```text
    TFR
     ^
TFRmax |---------------------------------------*** (飽和上限: 環境収容力)
       |                                   ***
       |                                ** 
       |                              ** (急峻立ち上がり: 黄金帯 1.40)
       |                           **
       |                         *
       |                       * (変曲点 SMI_0 ≈ 1.05)
TFRmin |--------------------***
       +---------------------------------------------> SMI
       0                   0.60   1.00  1.40    2.07
```[cite: 1, 2]

### 3.2 パラメータ確定値と物理的根拠

| パラメータ | 標準設定値 | 物理的・生物学的解釈 |
| :--- | :--- | :--- |
| $TFR_{min}$ | $0.65 \pm 0.05$ | 極限環境（$SMI \to 0$）における生物学的フロア値（韓国ソウル等で実測）[cite: 2, 4] |
| $TFR_{max}$ | $2.15 \pm 0.10$ | 現代都市型社会における制度的・生体収容力の上限（人口置換水準直上）[cite: 2, 5] |
| $SMI_0$ | $1.05 \pm 0.03$ | 関数の変曲点（Inflection Point）。生体防衛ブレーキが解除され始める境界線[cite: 2, 3] |
| $k$ | $4.00 \pm 0.25$ | 応答感度の急峻度（Hill係数に相当）。閾値付近で応答が相転移的に急変することを表す[cite: 2, 3] |

### 3.3 導関数（感度スペクトル）

SMIに対するTFRの限界感度 $\frac{d(TFR)}{d(SMI)}$ は以下のように与えられる[cite: 1, 2]。

$$\frac{d(TFR)}{d(SMI)} = \frac{k \cdot (TFR_{max} - TFR_{min}) \cdot \left(\frac{SMI}{SMI_0}\right)^{-(k+1)}}{SMI_0 \cdot \left[1 + \left(\frac{SMI}{SMI_0}\right)^{-k}\right]^2}$$

* **$SMI < 0.80$**: 感度はほぼゼロに漸近（どれほど小規模な給付金を投入してもTFRはピクリとも反応しない）[cite: 2, 4]。
* **$SMI \approx 1.05$**: 感度が極大値（最大傾斜）に達する。最も財政投入効率が高い変曲ゾーン[cite: 2, 4]。
* **$SMI > 1.80$**: 限界効果が逓減し、カーブは $TFR_{max}$ へ水平に飽和する（高所得層における少子化パラドックスの工学的解決）[cite: 2, 4]。

---

## 4. 時系列遅延分布モデル（Distributed Lag Model）

入力（SMI）から出力（TFR）までの遅延は、単一の固定値（4.0年）ではなく、配偶探索、婚姻手続き、妊娠、出産までの確率密度関数を内包した**「3〜5年の遅延分布結合」**として計算される[cite: 1, 2]。

### 4.1 伝達積分方程式

$$TFR_t = \int_{0}^{\infty} w(\tau) \cdot \Phi\Big(SMI(t - \tau)\Big) \, d\tau$$

離散化された年次統計モデルにおいては、以下の3〜5年有限インパルス応答（FIR）として実装する[cite: 1, 2]。

$$TFR_t = \sum_{\tau=3}^{5} w_\tau \cdot \Phi(SMI_{t-\tau})$$

$$\Phi(SMI) = 4PL(SMI)$$

$$\sum_{\tau=3}^{5} w_\tau = 1.0, \quad w_\tau > 0$$

### 4.2 標準ウェイト配分（Weight Vector）

計量経済バックテストおよび生物学的ロード時間（寿命の約5%）からキャリブレーションされた標準重み係数[cite: 1, 2]：

$$\mathbf{w} = \begin{bmatrix} w_3 \\ w_4 \\ w_5 \end{bmatrix} = \begin{bmatrix} 0.20 \\ 0.65 \\ 0.15 \end{bmatrix}$$

* $\tau = 4$（4年後）が主ピーク（$65\%$の寄与度）を形成する[cite: 1, 2]。
* グランジャー因果性検定（Granger Causality Test）において、$SMI_{t-4} \to TFR_t$ の有意水準は $p < 0.001$ を達成する[cite: 1, 2]。

---

## 5. 国際正規化プラグイン・アーキテクチャ (Normalization Plug-ins)

基礎式を破壊することなく、各国の特異な社会保障制度、税制、家族形態の差異を吸収するための共通インターフェース仕様を規定する[cite: 1, 2]。

```text
       [ 各国の公的統計 / 独自制度 ]
                     │
                     ▼
┌───────────────────────────────────────────────┐
│        正規化プラグイン (Plug-in Layer)        │
│  - 北欧・仏: 現物給付・保育無償化・事実婚補正  │[cite: 1, 2]
│  - 米国: 民間医療・学生ローン・所得階層分離    │[cite: 1, 2]
│  - 韓国: チョンセ保証金・極限私教育費補正      │[cite: 2, 5]
└───────────────────────────────────────────────┘
                     │
                     ▼
┌───────────────────────────────────────────────┐
│     SMI Core Engine (1階 共通無次元プロトコル)  │[cite: 1, 2]
│              SMI = WCI / C_surv_std           │[cite: 1, 2]
└───────────────────────────────────────────────┘

```

### 5.1 北欧・フランス型プラグイン（高福祉・高現物給付・事実婚）

北欧諸国やフランス等、公的セクターによる保育サービスの無償提供および事実婚制度（PACS等）が定着している国家群の補正プロトコル。

$$C_{surv\_nordic} = (C_{base} + C_{semi}) \cdot (1 - S_{gov}) \cdot \phi_{legal}$$

* **$S_{gov} \in [0.0, 0.5]$ (公的肩代わり率)**: 自治体・国家が提供する保育無償化、児童手当、公的住宅手当（APL等）の現物換算価値を生存固定費から控除。
* **$\phi_{legal} \approx 0.88$ (法的手続き・婚姻コスト免除係数)**: 事実婚が法的に完全保障され、婚姻に伴う法的・儀礼的摩擦コストが解消されている度合いを反映。

### 5.2 米国型プラグイン（民間医療保険・学生ローン・五分位分離）

全盲的な中央値ではなく、所得五分位（Quintile 1〜5）ごとに独立したSMIを算出し、学生ローンおよび民間医療保険負担を分母へ算入するプロトコル。

$$C_{surv\_us}(Q_k) = C_{base}(Q_k) + C_{semi}(Q_k) + C_{health\_private} + C_{student\_debt}$$

* **$C_{health\_private}$**: 民間健康保険の本人負担保険料および免責額（Deductible）の月割期待値。
* **$C_{student\_debt}$**: 若年層が抱える連邦・民間学生ローンの平均月間返済義務額。
* 米国では $Q_1, Q_2$（下位40%）のSMIが $0.50$ 未満に沈む一方、$Q_5$（上位20%）が $2.50$ を超えるという「階層相分離（Societal Bimodal Distribution）」を観測するための必須仕様となる。

### 5.3 韓国型プラグイン（伝染保証金・極限私教育費）

世界最低出生率（0.7前後）を記録する韓国の特殊事情を記述する補正。

$$C_{surv\_kr} = C_{base} + C_{semi} + \text{OpportunityCost}(Jeonse) + (\theta_{kr} \cdot R_{rel})$$

* **$\text{OpportunityCost}(Jeonse)$**: 住宅確保に必要な巨額のチョンセ（伝染）保証金に伴う借入金利、または機会損失コスト。
* **$\theta_{kr} \to 1.0$**: 熾烈な大学受験戦争（大峙洞塾街等）に伴う私立教育費が、実質的な必須固定費（分母）として不可避化している状態を記述。

---

## 6. 入出力データ型定義（JSON Schema 実装仕様）

SMI Layer 1 演算パイプラインに入力されるデータセットの完全なスキーマ定義。

```json
{
  "$schema": "[http://json-schema.org/draft-07/schema#](http://json-schema.org/draft-07/schema#)",
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

## 7. 結論と実装ガイドライン

本仕様書が規定する Layer 1 数理モデルは、経済的支援政策を「名目給付（手当）」から「分母解体（固定費削減）」へと転換させるための計算基盤である。

1. **API連携・ETLパイプラインの構築:** 各国の統計局API（e-Stat、OECD.Stat、BLS）から上記JSON Schemaへ変数をマッピングするスクリプトを記述すること。
2. **キャリブレーションの実施:** 各地域メッシュの実データを用い、4PLロジスティック関数の傾き $k$ および遅延重み $\mathbf{w}$ の局所最適化を行うこと。
3. **2階 Core Protocol への連携:** 本仕様書で算出された $SMI$ は、空間摩擦および相分離を扱う上位モジュール `SPECIFICATION_CORE.md` における基礎入力値（基底状態）として受け渡される。
