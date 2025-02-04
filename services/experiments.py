from models import Device, Experiment, ExperimentAssignment
from db import mongo


class ExperimentService:
    @staticmethod
    def assign_experiment(device_token):
        device = Device.get_by_token(device_token)

        if not device:
            with mongo.cx.start_session() as session:
                with session.start_transaction():
                    Device.create(device_token)
                    experiments_data = Experiment.generate_experiment_data()
                    ExperimentAssignment.create(device_token, experiments_data)
                    return experiments_data

        assignment = ExperimentAssignment.get_by_device_token(device_token)
        return assignment["experiments"]
