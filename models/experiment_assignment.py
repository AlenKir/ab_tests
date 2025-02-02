from datetime import datetime


def get_mongo():
    from app import mongo
    return mongo


class ExperimentAssignment:
    @staticmethod
    def get_by_device_token(device_token):
        return get_mongo().experiment_assignments.find_one({"device_id": device_token})

    @staticmethod
    def create(device_token, experiments_data):
        get_mongo().experiment_assignments.insert_one({
            "device_id": device_token,
            "experiments": experiments_data,
            "created_at": datetime.utcnow()
        })
