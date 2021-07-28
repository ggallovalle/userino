import logging
from typing import IO, Optional, Union
from os import PathLike
from backy.config.logger import create_logger
from dotenv.main import DotEnv, find_dotenv
from toolz.functoolz import memoize

from .models import Config, Environment, Db


def from_env(
    dotenv_path: Union[str, PathLike, None] = None,
    stream: Optional[IO[str]] = None,
    verbose: bool = False,
    interpolate: bool = True,
    encoding: Optional[str] = "utf-8",
) -> DotEnv:
    """
    Parse a .env file and return its content as a dict.

    - *dotenv_path*: absolute or relative path to .env file.
    - *stream*: `StringIO` object with .env content, used if `dotenv_path` is `None`.
    - *verbose*: whether to output a warning the .env file is missing. Defaults to
      `False`.
      in `.env` file.  Defaults to `False`.
    - *encoding*: encoding to be used to read the file.

    If both `dotenv_path` and `stream`, `find_dotenv()` is used to find the .env file.
    """
    if dotenv_path is None and stream is None:
        dotenv_path = find_dotenv()

    return DotEnv(
        dotenv_path=dotenv_path,
        stream=stream,
        verbose=verbose,
        interpolate=interpolate,
        override=True,
        encoding=encoding,
    )


@memoize
def get_config_from_dotenv() -> Config:
    config = from_env()
    if not config.set_as_environment_variables():
        logging.fatal("Environment variables couldn't be set")
    # use config[key] if you want to fail if environment variable isn't set
    # use config.get(key) if it can be None
    # use config.get(key, default) to provide a default
    config = config.dict()
    db = Db(url=config["DB_URL"])
    env = Environment(name=config["ENVIRONMENT"])
    config = Config(db=db, env=env)
    create_logger(env.name)
    return config
