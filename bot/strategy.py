import config.config as config
from utils.logger import log_event

def decide_action(index_value:int, has_position:bool, logger) -> str:
    if index_value <= config.BUY_THRESHOLD:
        action = "BUY" 
    elif index_value >= config.SELL_THRESHOLD and has_position:
        action = "SELL"
    else:
        action = "HOLD"
    log_event (
    logger,"strategy_decision", action=action, index_value=index_value 
    )
    return action

