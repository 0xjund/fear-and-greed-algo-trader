from moccasin.config import get_active_network

def get_price(feed_name:str) -> float:
    """
      Get a price feed from a contract and return a human readable number   
    """
    active_network = get_active_network()
    feed = active_network.manifest_named(feed_name)

    price = feed.latestAnswer()
    decimals = feed.decimals()

    return price / (10 ** decimals)
