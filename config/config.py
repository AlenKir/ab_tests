class Config:
    MONGO_URI = "mongodb://localhost:27017/ab_test_db"
    TESTING = False
    MONGO_DB_NAME = "ab_test_db"


class TestingConfig(Config):
    TESTING = True
    MONGO_URI = "mongodb://localhost:27017/TEST_ab_test_db"
    MONGO_DB_NAME = "TEST_ab_test_db"
