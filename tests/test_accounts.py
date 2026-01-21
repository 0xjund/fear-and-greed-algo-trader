import boa
from pathlib import Path

HERE = Path(__file__).resolve().parent
ABI_DIR = HERE.parent / "abis"

WBTC = "0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599"
WBTC_WHALE = "0x9ff58f4ffb29fa2266ab25e75e2a8b3503311656" 

def test_prank_behaviour():
    whale = WBTC_WHALE
    before = boa.env.eoa
    with boa.env.prank(whale):
        inside = boa.env.eoa
    after = boa.env.eoa

    assert before != whale
    assert str(inside).lower() == WBTC_WHALE.lower()
    assert after == before


def test_wbtc_transfer_from():
    factory = boa.load_abi(ABI_DIR / "wbtc.json")
    wbtc = factory.at(WBTC)

    whale_balance = wbtc.balanceOf(WBTC_WHALE)
    print("whale balance:", whale_balance)
    assert whale_balance > 0

    amount = 1
    recipient = boa.env.eoa

    # eth for gas
    boa.env.set_balance(WBTC_WHALE, 10**18)

    with boa.env.prank(WBTC_WHALE):
        ok = wbtc.transfer(recipient, amount)

    assert ok is True
    assert wbtc.balanceOf(recipient) == amount
