from datetime import datetime
from flask import Flask
from flask_pymongo import PyMongo

from config.config import Config
from routes.routes import ab_routes

mongo = PyMongo()


def setup_experiments():
    """Default experiments"""
    DEFAULT_EXPERIMENTS = {
        "button_color": {
            "options": {
                "#FF0000": 0.75,
                "#00FF00": 0.1,
                "#0000FF": 0.15
            }
        },
        "price": {
            "options": {
                "10": 0.75,
                "20": 0.1,
                "50": 0.05,
                "5": 0.1
            }
        }
    }

    for experiment_name, data in DEFAULT_EXPERIMENTS.items():
        existing_experiment = mongo.db.experiments.find_one({"experiment_name": experiment_name})
        if not existing_experiment:
            mongo.db.experiments.insert_one({
                "experiment_name": experiment_name,
                "options": data["options"],
                "created_at": datetime.utcnow()
            })


def create_app_with_config(config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config)
    mongo.init_app(app)
    setup_experiments()
    app.register_blueprint(ab_routes)
    return app


if __name__ == "__main__":
    app = create_app_with_config(Config)
    app.run(debug=True)
