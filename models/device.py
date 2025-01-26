from app import mongo


class Device:
    @staticmethod
    def get_by_token(device_token):
        return mongo.db.devices.find_one({"id": device_token})

    @staticmethod
    def create(device_token):
        mongo.db.devices.insert_one({"id": device_token})
