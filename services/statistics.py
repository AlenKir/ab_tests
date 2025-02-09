from db import mongo
from models import Experiment


class StatisticsService:
    @staticmethod
    def get_statistics():
        experiments = Experiment.get_experiments()

        statistics = []

        for experiment in experiments:
            experiment_name = experiment["name"]
            options = experiment["options"]
            total_devices = 0
            option_counts = {option: 0 for option in options}

            assignments = mongo.db.experiment_assignments.find({
                "experiments.{}".format(experiment_name): {"$exists": True}
            })

            for assignment in assignments:
                total_devices += 1
                assigned_option = assignment["experiments"][experiment_name]
                if assigned_option in option_counts:
                    option_counts[assigned_option] += 1

            statistics.append({
                "name": experiment_name,
                "total_devices": total_devices,
                "options": option_counts
            })

        return statistics
