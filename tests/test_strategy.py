from bot.strategy import decide_action
import pytest
import logging

@pytest.mark.parametrize(
    "index_value, has_position, expected", 
    [
        (10, False, "BUY"),
        (30, True, "HOLD"),
        (50, True, "HOLD"),
        (80, True, "SELL")
    ]
)

def test_strategy(index_value, has_position, expected):
    logger = logging.getLogger("dummy")

    action = decide_action(
        index_value=index_value,
        has_position=has_position,
        logger = logger 
        
    )
    
    assert action == expected

