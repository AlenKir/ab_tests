import random
from datetime import datetime


def get_mongo():
    from app import mongo
    return mongo


class Experiment:
    @staticmethod
    def create_experiment(name, options):
        experiment_data = {
            "experiment_name": name,
            "options": options,
            "created_at": datetime.utcnow()
        }
        get_mongo().experiments.insert_one(experiment_data)

    @staticmethod
    def get_experiments():
        return list(get_mongo().experiments.find())

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

            # print(f"Experiment: {experiment_name}, Selected option: {selected_option}")

        return results


