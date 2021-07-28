from flask.app import Flask
from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()


def setup_db(app: Flask) -> None:
    DB.init_app(app)


Base = DB.Model
