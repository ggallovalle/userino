from toolz.functoolz import memoize

from .logger import create_logger
from .models import Config, Environment


@memoize
def get_config_for_test(mock: Config) -> Config:
    env = Environment.build_test(mock.env.name)
    config = Config(db=mock.db, env=env)
    create_logger(env.name)
    return config
