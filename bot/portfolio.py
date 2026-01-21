import boa
from moccasin.config import get_active_network
from config.config import WBTC_DECIMALS, MIN_WBTC_POSITION

def get_wbtc_contract():
    """
      Fetch WBTC contract from the active network manifest  
    """
    active_network = get_active_network()
    return active_network.manifest_named("wbtc")

def get_wbtc_balance(address: str | None = None) -> int:
    """
    Return raw WBTC balance  
    """
    if address is None:
        address = boa.env.eoa

    wbtc = get_wbtc_contract()
    return wbtc.balanceOf(address)

def has_wbtc_position(min_balance: int = MIN_WBTC_POSITION, address: str | None = None) -> bool:
    """
       Check to see if the wallet holds WBTC above min
        
    """
    balance = get_wbtc_balance(address)
    return balance >= min_balance

def get_wbtc_human_balance(address: str | None = None) -> float:
    """
    Return a human readable balance  
    """
    balance = get_wbtc_balance(address)
    return balance / 10**WBTC_DECIMALS

def get_usdc_contract():
    """
      Fetch USDC contract from the active network manifest  
    """
    active_network = get_active_network()
    return active_network.manifest_named("usdc")

def get_usdc_balance(address: str | None = None) -> int:
    """
    Return USDC balance  
    """
    if address is None:
        address = boa.env.eoa

    usdc = get_usdc_contract()
    return usdc.balanceOf(address)

