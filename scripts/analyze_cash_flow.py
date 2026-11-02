"""Recalculate ratios and reconcile the source cash-flow statement (USD millions)."""
import json
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ADJUSTMENTS = (
    "depreciation_and_amortization", "share_based_compensation",
    "other_adjustments", "accounts_receivable", "vendor_non_trade_receivables",
    "inventories", "other_assets", "accounts_payable", "other_liabilities",
)


def main():
    data = json.loads((ROOT / "data/AAPL_cash_flows.json").read_text(encoding="utf-8"))
    ratios = []
    for row in data["periods"]:
        calculated = row["net_income"] + sum(row[key] for key in ADJUSTMENTS)
        if calculated != row["operating_cash_flow"]:
            raise ValueError(f"Cash-flow reconciliation failed: {row['fiscal_year']}")
        ratio = Decimal(row["operating_cash_flow"]) / Decimal(row["net_income"])
        ratios.append(ratio)
        print(f"FY{row['fiscal_year']} 9M: NI={row['net_income']:,}; "
              f"OCF={calculated:,}; OCF/NI={ratio:.4f} ({ratio * 100:.2f}%)")
    previous, current = data["periods"]
    print(f"Ratio change: {(ratios[1] - ratios[0]) * 100:+.2f} percentage points")
    print("Adjustment contribution changes (USD millions):")
    for key in ADJUSTMENTS:
        print(f"  {key}: {current[key] - previous[key]:+,}")
    observation = json.loads((ROOT / "observations/AAPL_FY2026_9M.json").read_text(encoding="utf-8"))
    for key in ("net_income", "operating_cash_flow"):
        if observation[key] != current[key]:
            raise ValueError(f"Observation mismatch: {key}")
    if Decimal(str(observation["cash_to_profit_ratio"])) != ratios[1].quantize(Decimal("0.0001")):
        raise ValueError("Observation ratio mismatch")
    print("Both cash-flow reconciliations and the current observation agree.")


if __name__ == "__main__":
    main()
