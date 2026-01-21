import pytest
from bot.portfolio import get_wbtc_contract, get_wbtc_balance, has_wbtc_position, get_wbtc_human_balance, get_usdc_balance, get_usdc_contract

def test_get_wbtc_contract(mocker):
    fake_contract = object()
    fake_network = mocker.Mock()
    fake_network.manifest_named.return_value = fake_contract 

    mocker.patch("bot.portfolio.get_active_network", return_value=fake_network)

    contract = get_wbtc_contract()

    fake_network.manifest_named.assert_called_once_with("wbtc")
    assert contract is fake_contract
    
def test_get_wbtc_contract_address(mocker):
    fake_contract = mocker.Mock()
    fake_contract.balanceOf.return_value = 123

    mocker.patch("bot.portfolio.get_wbtc_contract", return_value=fake_contract)

    balance = get_wbtc_balance("0xabc")

    fake_contract.balanceOf.assert_called_once_with("0xabc")
    assert balance == 123

def test_get_wbtc_balance_defaults_to_eoa(mocker):
    fake_contract = mocker.Mock()
    fake_contract.balanceOf.return_value = 456

    mocker.patch("bot.portfolio.get_wbtc_contract", return_value = fake_contract)
    mocker.patch("bot.portfolio.boa.env.eoa", "0xeoa")

    balance = get_wbtc_balance()

    fake_contract.balanceOf.assert_called_once_with("0xeoa")

    assert balance == 456

def test_get_wbtc_human_balance(mocker):
    mocker.patch("bot.portfolio.get_wbtc_balance", return_value = 123_000_000)
    mocker.patch("bot.portfolio.WBTC_DECIMALS", 8)

    balance = get_wbtc_human_balance()

    assert balance == 1.23


@pytest.mark.parametrize(
    "balance, min_balance, expected",
    [
        (100, 50, True),
        (50, 50, True),
        (40, 50, False)
    ]
)
def test_has_wbtc_position(mocker, balance, min_balance, expected):
    mocker.patch("bot.portfolio.get_wbtc_balance", return_value=balance)

    assert has_wbtc_position(min_balance=min_balance) is expected

def test_get_usdc_contract(mocker):
    fake_contract = object()
    fake_network = mocker.Mock()
    fake_network.manifest_named.return_value = fake_contract 

    mocker.patch("bot.portfolio.get_active_network", return_value=fake_network)

    contract = get_usdc_contract()

    fake_network.manifest_named.assert_called_once_with("usdc")
    assert contract is fake_contract
    
def test_get_usdc_contract_address(mocker):
    fake_contract = mocker.Mock()
    fake_contract.balanceOf.return_value = 1234

    mocker.patch("bot.portfolio.get_usdc_contract", return_value=fake_contract)

    balance = get_usdc_balance("0xabcd")

    fake_contract.balanceOf.assert_called_once_with("0xabcd")
    assert balance == 1234

