from utils.logger import setup_logger, log_event
from utils.api_client import fear_and_greed_index
from config.config import TRADE_PERCENT
from script.strategy import decide_action
from script.portfolio import has_wbtc_position, get_wbtc_human_balance  
from bot.pnl import snapshot_portfolio
from bot.trade import get_price, can_execute_trade

logger = setup_logger("test_logger")

index_value = fear_and_greed_index()

action = decide_action(index_value, has_wbtc_position, logger)

start_snapshot = snapshot_portfolio

price = get_price("WBTC_USD")

can_trade, reason = can_execute_trade (
    balance = get_wbtc_human_balance,
    trade_amount= TRADE_PERCENT,
    get_price=price
)

def log_price_observed(logger, feed, price):
    log_event(
    logger,
    "price_observed",
    feed = "WBTC_USD",
    price = price
    )

def log_trade(logger, can_execute_trade, price ):
    log_event(
        logger,
        "",
        price = price
    )

def log_single_swap_trade(logger, price, amount_out ):
    log_event(
        logger,
        ""
        ""
    )


def main():
        if __name__ == "__main__":
            main()
