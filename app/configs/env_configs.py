import os

from dotenv import load_dotenv
from flask import Flask

load_dotenv()


def init_app(app: Flask):

    app.config[
        'SQLALCHEMY_DATABASE_URI'
        ] = os.environ.get('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JSON_SORT_KEYS'] = False
