import json
import logging 
from utils.logger import setup_logger, log_event

def test_setup_logger_returns_logger():
    logger = setup_logger("test_logger")
    assert logger.name == "test_logger"

def test_log_event_emits_json(caplog):
    logger = setup_logger("test_logger", propagate=True)

    caplog.set_level(logging.INFO)

    log_event(
              logger,
              "strategy_decision",
              action = "BUY",
              index_value=42,)

    assert len(caplog.records) == 1

    payload = json.loads(caplog.records[0].message)
    assert payload["event"] == "strategy_decision"
