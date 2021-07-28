import logging

from toolz.functoolz import memoize

from .models import Config
from .models import Environment

LOGGER_NAME = "userino"


def get_logger_level_from_environment(env: str) -> int:
    if Environment.devp(env):
        return logging.DEBUG
    else:
        return logging.WARN


def create_logger(env: str) -> None:
    # see https://stackoverflow.com/questions/43109355/logging-setlevel-is-being-ignored
    logging.basicConfig(level=logging.DEBUG)
    userino = logging.getLogger(LOGGER_NAME)
    level = get_logger_level_from_environment(env)
    userino.setLevel(level)
    userino.debug("Logger is configured")


def logger() -> logging.Logger:
    return logging.getLogger(LOGGER_NAME)
