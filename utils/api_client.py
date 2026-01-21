import httpx
from utils.logger import log_event

def fear_and_greed_index() -> int:
    """Fetch current fear and greed index value(0-100)"""
    response = httpx.get('https://api.alternative.me/fng/?limit=1')
    if response.status_code != 200:
        raise Exception(f"API request failed with status {response.status_code}")

    data = response.json()
    return int(data['data'][0]['value'])
