from dataclasses import asdict

from backy.config import get_config_from_dotenv


def welcome() -> str:
    return "Welcome to Userino Backend"


def env():
    return asdict(get_config_from_dotenv())
