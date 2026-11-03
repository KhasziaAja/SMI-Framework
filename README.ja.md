# SMI Framework (Social Margin Index) - v1.0 [Open Standard]

[English](./README.md) | [日本語](./README.ja.md)

> **"社会の存続と崩壊は、道徳や意識変化（ポエム）ではなく、個体の可処分生存エネルギー（物理量）で決定される。"**

SMI Framework は、高度資本主義社会における少子化、未婚化、人口急減、および社会システムの機能不全メカニズムを、感情論を排した「エネルギー収支」として定量化・予測・シミュレーションするためのオープンソース・社会工学標準プロトコル（State OS基幹アーキテクチャ）である[cite: 1, 2, 5]。

---

## 1. 宣言と適用境界条件（System Philosophy & Boundary Conditions）

### 1.1 宣言：生体防衛ブレーキの解除
現代の先進国および都市化社会において、少子化や婚姻率低下は「若者の草食化」「価値観の多様化」「子育て支援の不足」といった情緒的解釈（言語的ポエム）によって議論されてきた[cite: 1, 2, 5]。しかし、対症療法的な給付金や啓発キャンペーンを投下しても、出生動態の急落は停止していない[cite: 1, 5]。

人間という生物（大型哺乳類・K戦略種）において、生殖・長期投資・世帯形成は、個体の生存基盤が脅かされた際に前頭前野および自律神経系（HPA軸）が作動させる**「生体防衛ブレーキ（Autonomic Shutdown：自律停止）」**によって物理的に遮断される[cite: 1, 2, 5]。

本プロトコルは、特定の政治思想や道徳観を強制するものではない[cite: 5]。通貨や物価水準に依存しない**無次元の物理メーター（バイタルモニター）**を社会工学に導入し、国家・自治体・組織の構造的デバッグを実行するための共通言語を提供する[cite: 1, 2, 5]。

### 1.2 動作環境を定義する3大適用境界条件
本モデルは、無条件にあらゆる社会・文明で動作する抽象論ではなく、以下の3大条件を満たす「近代都市資本主義社会」を前提動作環境（OS）として規定する[cite: 1, 5]。

1. **貨幣・市場決済経済（Monetized Society）：** 生存・再生産に必要な固定費の大半が市場を介し法定通貨で決済されていること（自給自足農村や配給制共産圏は対象外）[cite: 1, 5]。
2. **個体の自由意志と契約自律性（Individual Autonomy）：** 未婚・不婚・避妊・生活様式の選択権が個体に担保されていること（奴隷制や宗教的強制生殖コミュニティは対象外）[cite: 1, 5]。
3. **子どもの構造的純負債化（Child Net Cost / $P_{net} < 1.0$）：** 児童労働の禁止と義務教育により、子どもが成人まで一方的な消費主体（固定費）であること（子どもが5歳から労働力として分子に貢献する伝統的農村は対象外）[cite: 1, 2, 5]。

---

## 2. 基礎方程式（1階モデル：SMI Lite）

個体（若年単身層）の獲得可能エネルギーと、社会が要求する不可避の生存維持コストの比率を **SMI (Social Margin Index)** と定義する[cite: 1, 5]。

$$SMI = \frac{WCI}{C_{surv\_std}} = \frac{WCI}{C_{base} + C_{semi}}$$

### 変数定義（Variables）

* **$WCI$ (Working Capital Income：実効可処分所得中央値)**  
  対象地域における若年単身層（25〜34歳）の、税・社会保険料を控除した実効手取り中央値[cite: 1, 2, 5]。
* **$C_{surv\_std}$ (標準生存維持費用：Standard Survival Cost)**  
  公的扶助（生活保護）水準ではなく、個体が心身の健康と適正な自立・社会参加を維持するための標準固定費[cite: 1, 2]。
  $$C_{base} = C_{rent} + C_{food\_min} + C_{infra\_vital}$$
  $$C_{semi} = C_{tax\_ins} + C_{depr} + C_{conn} + (\theta \cdot R_{rel})$$
  * $C_{rent}$: 民間適正家賃（単身25〜30㎡水準の中央値）[cite: 1, 2]
  * $C_{food\_min}$: 基礎栄養維持費（自炊ベースの必須カロリー支出）
  * $C_{infra\_vital}$: 生存必須光熱水道費[cite: 5]
  * $C_{tax\_ins}$: 限界的な税・社会保険料負担実効額[cite: 1, 2]
  * $C_{depr}$: 自衛減価償却引当（敷金更新料、家電更新、予防医療、冠婚葬祭積立）[cite: 1, 2]
  * $C_{conn}$: 就業・社会維持に不可欠な通信インフラ費
  * $\theta \cdot R_{rel}$: 相対的標準コスト項（周囲の教育投資競争・世間体摩擦）[cite: 3, 4]

> **注記（公的CPIによる実質化の排除）：**  
> 本モデルにおける分母（$C_{surv\_std}$）は、公的総合CPIによるデフレートを意図的に排除している[cite: 4]。耐久消費財の低価格化で希釈される公的CPIではなく、生体OSが直接感知する「回避不能な4大固定費（都市適正家賃・税社保限界負担・必須インフラ・予防医療教育引当）」に限定した実物バスケット（生体生存固定費）として直接算定・評価する[cite: 4]。

---

## 3. 4大相転移閾値（Phase Transition Thresholds）

SMIは通貨単位を相殺した無次元数（純粋倍率）であり、時代や為替、国境を超えて以下の物理境界線（相転移点）として機能する[cite: 1, 2]。

| SMI スコア | システム状態 | 生体・社会の挙動 |
| :--- | :--- | :--- |
| **$SMI < 0.60$** | **自律停止・身食い圏** | 単身個体の維持すら将来の減価償却を削る延命状態。脳が強烈な防衛ブレーキを踏み、婚姻・生殖・長期投資行動を物理的に自律遮断する（東アジア大都市部の現状）[cite: 1, 2, 5]。 |
| **$1.00 \le SMI < 1.40$** | **空荷自立・防衛限界線** | 1人分の生活を維持できるが、他者を背負うバッファー（余白）がゼロ。交際や世帯形成へのエントリー権が発生せず、現状維持に固定される[cite: 1, 2, 5]。 |
| **$1.40 \le SMI < 2.07$** | **再生産・世帯形成黄金帯** | 個体維持費を超過する40%以上の余剰エネルギーが恒常的に担保される領域。OECD等価尺度（世帯形成コスト $+0.4$）と数学的に同型であり、人口置換水準（TFR 2.07）への回復が可能となる[cite: 1, 2, 5]。 |
| **$SMI \ge 2.07$** | **有事インパルス・ブースト域** | 長年の低SMIにより自律停止に陥った社会を解凍するための過渡的過充電モード（3〜5年の時限措置）。前頭前野のトラウマを強制解除する[cite: 1, 2, 5]。 |

---

## 4. 伝達関数と時間軸ダイナミクス

### ① TFR応答（4パラメータ・ロジスティック関数）
SMIの向上に対する出生率（TFR）の応答は、線形（直線）ではなく上限飽和を伴うS字シグモイド曲線（4PL）を描く[cite: 1, 2]。

$$TFR(SMI) = TFR_{min} + \frac{TFR_{max} - TFR_{min}}{1 + \left(\frac{SMI}{SMI_0}\right)^{-k}}$$

* $SMI_0 \approx 1.05$（変曲点：繁殖ロックの解除開始ライン）[cite: 2, 3]
* $k \approx 4.0$（Hill係数に相当する急峻度パラメータ）[cite: 2, 3]
* $TFR_{min} \approx 0.65$（極限環境における生物学的フロア値）[cite: 2, 4]
* $TFR_{max} \approx 2.15$（都市型社会の制度的・生体収容力天井）[cite: 2, 5]

### ② 時系列遅延分布（Distributed Lag Model）
人間（K戦略大型哺乳類）の生命史制約に基づき、環境好転（SMI上昇）から初産（TFR上昇）までのシステムレイテンシは、成体寿命の約5%（$t+3 \sim 5$ 年、主ピーク4年）の遅延分布として表れる[cite: 1, 2, 8]。

$$TFR_t = \sum_{\tau=3}^{5} w_\tau \cdot 4PL(SMI_{t-\tau}) \quad (w_3 = 0.20, \ w_4 = 0.65, \ w_5 = 0.15)$$[cite: 1, 2]

---

## 5. 入出力データ仕様（JSON Schema）

SMI計算エンジンの入出力インターフェースは以下の規格に準拠する[cite: 1, 2]。

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

## 6. 学術別クイックナビゲーション（Academic Gateways）

各専門領域の研究者は、関心のある詳細ドキュメントへ直接アクセスされたい。

* 📊 **計量経済学 / 人口統計学の方へ:**  
  $\to$ [`docs/ja/SPECIFICATION_LITE.ja.md`](./docs/ja/SPECIFICATION_LITE.ja.md)  
  公的統計（家計調査、CPS、OECD）からの $WCI$ / $C_{surv}$ 自動抽出仕様、および時系列遅延分布の回帰仕様。
* 🧬 **進化生物学 / 行動生態学の方へ:**  
  $\to$ [`docs/ja/PHILOSOPHY_AND_DYNAMICS.ja.md`](./docs/ja/PHILOSOPHY_AND_DYNAMICS.ja.md)  
  生活史理論（Life History Theory）、K戦略哺乳類の寿命5%ラグ、エネルギー配分制約[cite: 1, 4, 7]。
* 🧠 **脳神経科学 / 行動経済学の方へ:**  
  $\to$ [`docs/ja/PHILOSOPHY_AND_DYNAMICS.ja.md`](./docs/ja/PHILOSOPHY_AND_DYNAMICS.ja.md)  
  スキャシティ（欠乏）ストレス、前頭前野の認知帯域（Bandwidth）強制徴用、HPA軸による繁殖自律停止[cite: 4, 7, 8]。
* 📐 **複雑系科学 / 数理物理学の方へ:**  
  $\to$ [`docs/ja/SPECIFICATION_LITE.ja.md`](./docs/ja/SPECIFICATION_LITE.ja.md)  
  4PLロジスティック関数、非線形飽和、相転移解析[cite: 4, 6]。
* 🛠️ **オープンIssue / 反証テストに参加される方へ:**  
  $\to$ [`docs/ja/BENCHMARK_AND_ISSUES.ja.md`](./docs/ja/BENCHMARK_AND_ISSUES.ja.md)  
  全14項目のオープンIssueリスト、厳格な反証可能性基準、推奨公的データセット[cite: 1, 4, 7]。

---

## 7. 構造的拡張：2階（Core Kernel）プロトコルについて

本公開リポジトリで提供しているSMIモデル（1階）は、個人の経済的余剰と繁殖動態を制御する「基盤OS」です[cite: 1, 15]。

しかし、実際の国家・地域動態においては、単なる経済コストだけでなく、
**「空間的集積度」「文化・法規範距離」「社会的摩擦コスト（Toxicity）」**
が内生変数として作用し、特定の相転移（Phase Transition / 自治区化）を引き起こします[cite: 1, 15]。

当プロジェクトでは、1階のSMIに対し、以下の要素を統合した**「Core Kernel（2階プロトコル）」**を別途定義・保持しています[cite: 1, 15]。

* 非線形空間摩擦関数 $\text{Toxicity}(m, t)$ の完全展開式
* 空間相分離・自治区化判定アルゴリズム（Phase 1〜3 / Point of No Return）
* 20年第一崩壊線・世代交代弾道予測モデル

---

### 🔒 2階仕様書・研究Issueへのアクセス申請（Access Request）

国家安全保障および主権保護の観点から、2階プロトコルの完全仕様書（`SPECIFICATION_CORE.md`）およびプライベート開発ボードは、身元（所属・GitHubアカウント等）を提示できる研究機関・政策実務家・アナリスト・適格共同開発者にのみ個別に開示しています[cite: 11, 15]。

閲覧・検証を希望される方は、以下の公式ゲートウェイよりアクセス申請を行ってください[cite: 11, 15]。

👉 **[Layer 2 Core Protocol アクセス審査申請フォーム](https://forms.gle/tHVG5mxRhNGaQpfeA)**
*(※ 独立運用のため、内容確認およびリポジトリ招待の発行までに一定のお時間をいただく場合があります)*

---

## 8. 専門的議論への参加（Discussions & Call for PRs）

本プロトコルは、概念の定式化（アーキテクチャ設計）を主目的としている。

公的統計（国勢調査・家計調査・OECD）を用いた計量バックテスト、パラメータのキャリブレーション、およびシミュレーション実装に関するプルリクエスト（PR）やIssueでの議論を歓迎する。

* **数理・関数の改善提案** ➔ `Model & Math Calibration` カテゴリへ
* **統計抽出パイプラインの共有** ➔ `Data Pipelines & Normalization` カテゴリへ
* **生体・神経メカニズムの検証** ➔ `Biological & Cognitive Mechanisms` カテゴリへ

---

## 9. ライセンス（License）

* **1階オープンモデル（SMI Base Standard）：** [MIT License](./LICENSE)  
  学術利用、引用、派生研究、民間システムへの組み込みは自由に許可される[cite: 1, 5]。
* **2階コアモジュール（State OS Core Kernel）：** All Rights Reserved（限定審査制）[cite: 4, 5]
