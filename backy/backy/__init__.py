__version__ = "0.1.0"

from backy.app import setup_flask
from backy.config import get_config_from_dotenv


APP = setup_flask(get_config_from_dotenv())
