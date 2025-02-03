from datetime import datetime
from db import mongo


class ExperimentAssignment:
    @staticmethod
    def get_by_device_token(device_token):
        return mongo.db.experiment_assignments.find_one({"device_id": device_token})

    @staticmethod
    def create(device_token, experiments_data):
        mongo.db.experiment_assignments.insert_one({
            "device_id": device_token,
            "experiments": experiments_data,
            "created_at": datetime.utcnow()
        })
