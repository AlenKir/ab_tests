from datetime import datetime
from typing import Dict

from flask_pymongo import PyMongo

mongo = PyMongo()

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


def setup_experiments(mongo):
    for experiment_name, data in DEFAULT_EXPERIMENTS.items():
        existing_experiment = mongo.db.experiments.find_one({"name": experiment_name})
        if not existing_experiment:
            mongo.db.experiments.insert_one({
                "name": experiment_name,
                "options": data["options"],
                "created_at": datetime.utcnow()
            })
