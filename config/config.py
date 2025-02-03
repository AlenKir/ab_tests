class Config:
    MONGO_URI = "mongodb://localhost:27017/ab_test_db"
    TESTING = False


class TestingConfig(Config):
    TESTING = True
    MONGO_URI = "mongodb://localhost:27017/TEST_ab_test_db"
