from datetime import datetime
from flask import Flask
from db import mongo, setup_experiments

from config.config import Config
from routes.routes import ab_routes


def create_app_with_config(config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config)
    mongo.init_app(app)
    setup_experiments(mongo)
    app.register_blueprint(ab_routes)
    return app


if __name__ == "__main__":
    app = create_app_with_config(Config)
    app.run(debug=True)
