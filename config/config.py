from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    MONGO_URI = os.getenv("MONGO_URI")
    MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")
    TESTING = False


class TestingConfig(Config):
    MONGO_URI = os.getenv("TEST_MONGO_URI")
    MONGO_DB_NAME = os.getenv("TEST_MONGO_DB_NAME")
    TESTING = True
