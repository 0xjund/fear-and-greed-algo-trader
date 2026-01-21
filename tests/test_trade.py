import boa
from bot.trade import swap_exact_input_single
from pathlib import Path

HERE = Path(__file__).resolve().parent
ABI_DIR = HERE.parent / "abis"

WBTC = "0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599"
WBTC_WHALE = "0x9ff58f4ffb29fa2266ab25e75e2a8b3503311656" 
UNISWAP_ROUTER = "0xE592427A0AEce92De3Edee1F18E0157C05861564"
UNISWAP_FACTORY = "0x1F98431c8aD98523631AE4a59f267346ea31F984"
USDC = "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48"

def test_wbtc_to_usdc_trade():
    router = boa.load_abi(ABI_DIR / "uniswap_swap_router.json").at(UNISWAP_ROUTER)
    factory = boa.load_abi(ABI_DIR / "uniswap_v3_factory.json").at(UNISWAP_FACTORY)

    wbtc = boa.load_abi(ABI_DIR / "wbtc.json").at(WBTC)
    usdc = boa.load_abi(ABI_DIR / "usdc.json").at(USDC)

    pool = factory.getPool(WBTC, USDC, 3000)
    assert pool != "0x0000000000000000000000000000000000000000"

    amount_in = 1_000_000 # 0.01 WBTC

    boa.env.set_balance(WBTC_WHALE, 10**18)

    with boa.env.prank(WBTC_WHALE):
        assert wbtc.balanceOf(WBTC_WHALE) >= amount_in

        amount_out = swap_exact_input_single(
        router,
        wbtc,
        usdc,
        amount_in,
        0,
        3000,
    )

    
    assert amount_out > 0
    assert usdc.balanceOf(WBTC_WHALE) > 0
    
