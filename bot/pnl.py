from dataclasses import dataclass
from utils.get_price import get_price
from bot.portfolio import get_usdc_balance, get_wbtc_balance, WBTC_DECIMALS

@dataclass
class PortfolioSnapShot:
    usdc: int
    wbtc: int
    total_usd: float

def snapshot_portfolio() -> PortfolioSnapShot:
    usdc = get_usdc_balance
    wbtc = get_wbtc_balance

    wbtc_price = get_price("wbtc_usd")

    total_usd = (
        usdc/ 1e6
        + (wbtc / 10**WBTC_DECIMALS) * wbtc_price
    )

    return PortfolioSnapShot(
        usdc = usdc,
        wbtc = wbtc,
        total_usd=total_usd
    )

