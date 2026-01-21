import boa
import time
import config.config as config
from moccasin.config import get_active_network

SIX_DECIMALS = 1_000_000
EIGHTEEN_DECIMALS = 1_000_000_000_000_000_000

def get_price(feed_name: str) -> float:
    """Using the name of the price feed, we return an integer (no decimals) to get the
    approximate price of an asset.

    Args:
        feed_name (str): The name of the price feed
    Returns:
        float: The price of the asset in USD
    """
    # Get prices
    active_network = get_active_network()
    price_feed = active_network.manifest_named(feed_name)
    price = price_feed.latestAnswer()
    decimals = price_feed.decimals()
    decimals_normalized = 10**decimals
    return price / decimals_normalized

def can_execute_trade(balance, trade_amount, get_price) -> bool:
    """Check to see if we can cover the ETH for trade and gas"""
    gas_price = boa.env.get_gas_price()
    gas_price_gwei = gas_price / 10**9

    if gas_price_gwei > config.MAX_GAS_PRICE_GWEI:
        # Add log 
        return False, "Gas Price too High"

    if balance < config.MIN_BALANCE_ETH:
        # Add log 
        print(f"Balance of: {balance} is too low, need a minimum balance of {config.MIN_BALANCE_ETH})")
        return False
    
    if trade_amount < config.MIN_TRADE_SIZE:
        # Add log
        print(f"The trade amount is too small: {trade_amount}")
        return False
        
def swap_exact_input_single(
    swap_router,
    token_in_contract,
    token_out_contract,
    amount_in: int,
    amount_out_min: int,
    pool_fee: int = 3000,  # 0.3% fee tier
) -> int:
    """
    Swaps a fixed amount of token_in for a maximum possible amount of token_out

    Args:
        swap_router: ISwapRouter contract
        token_in_contract: Input token contract
        token_out_contract: Output token contract
        amount_in: Exact amount of input token to swap
        pool_fee: Fee tier (default 0.3% = 3000)

    Returns:
        amount_out: Amount of output token received
    """
    # First approve router to spend token
    token_in_contract.approve(swap_router.address, amount_in)

    deadline = int(time.time()) + 60
    
    amount_out = swap_router.exactInputSingle(
        (
            token_in_contract.address,
            token_out_contract.address,
            pool_fee,
            boa.env.eoa,
            deadline, 
            int(amount_in),
            int(amount_out_min),
            0,
        )
    )
    return amount_out
