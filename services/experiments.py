from models import Device, Experiment, ExperimentAssignment


class ExperimentService:
    @staticmethod
    def assign_experiment(device_token):
        device = Device.get_by_token(device_token)

        if not device:
            Device.create(device_token)
            experiments_data = Experiment.generate_experiment_data()
            ExperimentAssignment.create(device_token, experiments_data)
            return experiments_data

        assignment = ExperimentAssignment.get_by_device_token(device_token)
        return assignment["experiments"]
