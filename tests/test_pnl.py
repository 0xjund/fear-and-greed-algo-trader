from bot.pnl import PortfolioSnapShot


def test_pnl_match():
    start = PortfolioSnapShot(0, 0, 1000.0)
    now = PortfolioSnapShot(0, 0, 1100.0)

    assert now.total_usd - start.total_usd == 100.0
