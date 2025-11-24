import requests

def get_fear_and_greed_index_reading() -> int:
    """Fetch current fear and greed index value(0-100)"""
    response = requests.get('https://api.alternative.me/fng/?limit=1')
    if response.status_code != 200:
        raise Exception(f"API request failed with status {response.status_code}")

    data = response.json()
    return int(data['data'][0]['value'])

daily_index_reading = get_fear_and_greed_index_reading()



    
