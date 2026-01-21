import logging
import json

def setup_logger(name: str = "trading_bot", propagate: bool = False) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    logger.propagate = propagate
    return logger 

def log_event(logger: logging.Logger, event: str, **data):
    payload = {
        "event": event,
        **data
    }
    logger.info(json.dumps(payload))


