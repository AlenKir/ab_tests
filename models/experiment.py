import random
from datetime import datetime
from db import mongo


class Experiment:
    @staticmethod
    def create_experiment(name, options):
        experiment_data = {
            "experiment_name": name,
            "options": options,
            "created_at": datetime.utcnow()
        }
        mongo.db.experiments.insert_one(experiment_data)

    @staticmethod
    def get_experiments():
        return list(mongo.db.experiments.find())

    @staticmethod
    def generate_experiment_data():
        experiments = Experiment.get_experiments()

        if not experiments:
            return None

        results = {}

        for experiment in experiments:
            experiment_name = experiment['experiment_name']
            options = experiment["options"]
            values = list(options.keys())
            probabilities = list(options.values())

            selected_option = random.choices(values, probabilities)[0]
            results[experiment_name] = selected_option

        return results
