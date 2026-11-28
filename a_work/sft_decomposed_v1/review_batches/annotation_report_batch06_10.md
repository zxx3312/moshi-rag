# Batch 6–10 审核结果

用户已于 2026-11-28 确认审核通过。本轮按最新 Note 落实七题处理，清除当前五批的待审核状态。原题、上下文、旧 gold 与原始模型输出保留。

## 七题处理

### [batch_06 第 2 题](batch_06/batch_06.md)

保留两单元及当前修正描述：Paul Robeson 是已宣布音乐会的演出者；不要求证明他本人发布公告。

### [batch_06 第 15 题](batch_06/batch_06.md)

按 Note 严格依据 context。u1 为歌曲 Jimmy Choo；u2 无命名关系直接证据，取消预设路径，答案留空，完整 context 下仍为 UNRESOLVED。旧 gold 的 Jimmy Choo 仅作历史参考。

### [batch_07 第 17 题](batch_07/batch_07.md)

按 Note 同时回答学校和地区：两个单元均为 necessary=true，保留地区对学校的依赖；答案为 Purcell School 和 Hertfordshire，均由 d4s0 支持。

### [batch_08 第 1 题](batch_08/batch_08.md)

按用户确认，将 d2s2 与 d4s0 的联合推断作为 u1 的 context 支持；两条证据必须同时到达。移除 by_presupposition 和 presupposition_sets，答案仍为 TAAG Angola Airlines。

### [batch_09 第 29 题](batch_09/batch_09.md)

按 Note 采用 context 的影片年份口径：1974 与 2008，结论 Upasane；2016 为美国院线上映年份，不作为 2008 的别名。

### [batch_10 第 2 题](batch_10/batch_10.md)

按 Note 保留 private 及已有别名作为标注目标，结论必须由两方类别证据支持；不声称这是自然语言中唯一可能的共同类别。

### [batch_10 第 24 题](batch_10/batch_10.md)

按 Note 保留原问题措辞，采用人物→以其宣言命名的乐队两步解释；最终 S.C.U.M 由 d4s0/d4s3 支持，不把它说成以 Valerie Solanas 本人姓名命名。

## 使用说明

审核完成不等于每个单元都有足够证据。6-15 的 u2 已取消预设支持，expected_answer=null、support_sets=[]，完整上下文下仍应为 UNRESOLVED；重建 SFT 时必须保留这一含义，不能填回旧答案作为有支持目标。

本次调整为单元标注，逐时刻 SFT 尚未重建，未训练。原始 train/dev 导出和 B 文件未修改。修改前文件见 annotation_audit/before_user_confirmation_20261128.json；历史审阅记录保留原状态作为追溯材料，不是当前审核状态。
