from utils.api_client import fear_and_greed_index

def test_fear_and_greed_range():
    value = fear_and_greed_index()
    assert 0 <= value <= 100
    
    
