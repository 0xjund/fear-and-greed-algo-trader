import boa
from boa.contracts.abi.abi_contract import ABIContract
from moccasin.config import get_active_network, get_config, _Networks
from script._setup_script import setup_script
from utils.api_client import daily_index_reading

SIX_DECIMALS = 1_000_000
EIGHTEEN_DECIMALS = 1_000_000_000_000_000_000
MIN_BALANCE_ETH = 0.05
MIN_TRADE_SIZE = 0.01

def get_price(feed_name: str) -> float:
    """Using the name of the price feed, we return an integer (no decimals) to get the
    approximate price of an asset.

    Args:
        feed_name (str): The name of the price feed
    Returns:
        float: The price of the asset in USD
    """
    # config = get_config()
    # config._load_config(config.config_path)
    # config.networks = _Networks(config._toml_data, config.project_root)

    # Get prices
    active_network = get_active_network()
    price_feed = active_network.manifest_named(feed_name)
    price = price_feed.latestAnswer()
    decimals = price_feed.decimals()
    decimals_normalized = 10**decimals
    return price / decimals_normalized

def can_execute_trade(balance, trade_amount):
    """Check to see if we can cover the ETH for trade and gas"""
    # Check to see if I can get this through titanaboa
    estimated_gas_cost = 0.01

    if balance < MIN_BALANCE_ETH:
        print(f"Balance of: {balance} is too low, need a minimum balance of {MIN_BALANCE_ETH})")
        return False

    if trade_amount < MIN_TRADE_SIZE:
        print(f"The trade amount is too small: {trade_amount}")
        return False

def check_daily_reading(int: daily_index_reading) -> bool:
    pass 
 
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

    # struct ExactInputSingleParams {
    #     address tokenIn;
    #     address tokenOut;
    #     uint24 fee;
    #     address recipient;
    #     uint256 amountIn;
    #     uint256 amountOutMinimum;
    #     uint160 sqrtPriceLimitX96;
    # }
    amount_out = swap_router.exactInputSingle(
        (
            token_in_contract.address,
            token_out_contract.address,
            pool_fee,
            boa.env.eoa,
            int(amount_in),
            int(amount_out_min),
            0,
        )
    )
    return amount_out

def moccasin_main():
    usdc, wbtc  = setup_script()
