from datetime import datetime


def get_mongo():
    from app import mongo
    print('get_mongo')
    print(type(mongo))
    return mongo.db


class Device:
    @staticmethod
    def get_by_token(device_token):
        db = get_mongo()
        print(type(db))

        return get_mongo().devices.find_one({"id": device_token})

    @staticmethod
    def create(device_token):
        get_mongo().devices.insert_one({"id": device_token, "created_at": datetime.utcnow()})
