# -*- coding: UTF-8 -*-
from flask import Flask
from flask_session import Session

from config import config

session = Session()


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    session.init_app(app)

    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

