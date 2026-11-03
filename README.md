# FinQuant-Lab

用可追溯数据练习企业财务分析。本仓库的第一条模拟观察记录分析苹果 2026 与 2025 财年前九个月的现金创造能力。

- [企业负债分析模板](templates/corporate_liability_analysis.md)：研究公司时，先将负债分为经营性负债、借款和其他负债，再结合履行方式、到期时间与现金流判断风险。复制到 `reports/` 后填写，保留来源及未核实事项。

- [分析报告](reports/AAPL_FY2026_9M.md)：计算、差异归因与后续观察。
- [结构化观察记录](observations/AAPL_FY2026_9M.json)：本期指标与模拟总结。
- [现金流数据](data/AAPL_cash_flows.json)：两期原始数值、单位和来源。
- [复算脚本](scripts/analyze_cash_flow.py)：使用 Python 标准库复算比率并核对现金流勾稽。

在仓库根目录运行：

```sh
python scripts/analyze_cash_flow.py
```

金额单位为百万美元；期间为财年前九个月，不能与单季度混用。模拟观察指学习用记录，财务数值取自所列 SEC 来源；不代表实际交易或投资建议。
