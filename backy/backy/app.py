from backy.config.logger import logger
from flask import Flask

from backy.config import Config
from backy.models import setup_db
from backy.routes import env, welcome


def add_routes(app: Flask) -> None:
    app.add_url_rule("/", view_func=welcome)
    app.add_url_rule("/env", view_func=env)


def setup_flask(config: Config) -> Flask:
    if config.env.is_dev():
        logger().info(config)
    app = Flask(__name__)
    # setup_db(app)

    add_routes(app)
    return app
