from flask import Flask
from app.configs import env_configs, database, migrate
from app.routes import lead_blueprint


def create_app():
    app = Flask(__name__)

    env_configs.init_app(app)
    database.init_app(app)
    migrate.init_app(app)
    app.register_blueprint(lead_blueprint.bp)

    return app
