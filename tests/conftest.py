import os
import pytest
import boa
import sys
from pathlib import Path
from dotenv import load_dotenv

# Add the parent directory (project root) to the Python path
sys.path.insert(0, str(Path(__file__).parent.parent))

load_dotenv()

@pytest.fixture(scope="session", autouse=True)
def fork_mainnet():
    rpc = os.environ["MAINNET_RPC_URL"]
    boa.fork(rpc)
    yield



# @pytest.fixture(scope="function")
# def swap_router():
#     # Uni V3 swap router
#     swap_router = boa.env.manifest_named("uniswap_swap_router")

#     return swap_router

# @pytest.fixture(scope="function")
# def tokens():
#     usdc = boa.env.manifest_named("usdc")
#     wbtc = boa.env.manifest_named("wbtc")

#     return usdc, wbtc

# @pytest.fixture(scope="function")
# def seeded_tokens(tokens):
#     usdc, wbtc = tokens

#     # Mainnet Whale accounts
#     wbtc_whale = "0xF977814e90dA44bFA03b6295A0616a897441aceC"
#     usdc_whale = "0x55fe002aeff02f77364de339a1292923a15844b8" 
    
#     # Fund eth
#     boa.env.set_balance(wbtc_whale, 10**19)
#     boa.env.set_balance(usdc_whale, 10**19)

#     assert wbtc.balanceOf(wbtc_whale) > 0
#     assert usdc.balanceOf(usdc_whale) > 0

#     with boa.env.prank(wbtc_whale):
#         wbtc.transfer(boa.env.eoa, 1 * 10**8)

#     with boa.env.prank(usdc_whale):
#         usdc.transfer(boa.env.eoa, 100_000 * 10**6)

#     return usdc, wbtc

# @pytest.fixture(scope="function")
# def swap_context(seeded_tokens):
#     usdc, wbtc = seeded_tokens
#     router = boa.manifest_named("uniswap_swap_router")
#     return router, wbtc, usdc
