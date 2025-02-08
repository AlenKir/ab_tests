import mongomock
import pytest

import sys
import os

from flask.testing import FlaskClient
from pymongo import MongoClient

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app_with_config
from config.config import TestingConfig

from db import mongo, setup_experiments


@pytest.fixture()
def app(request):
    test_app = create_app_with_config(TestingConfig)
    with test_app.app_context():
        yield test_app


@pytest.fixture
def client(app) -> FlaskClient:
    return app.test_client()


@pytest.fixture(autouse=True)
def patch_mongo(monkeypatch):
    test_client = MongoClient(TestingConfig.MONGO_URI)
    db = test_client.get_database()
    setup_experiments(db)

    def fake_mongo():
        return test_client

    monkeypatch.setattr('db.mongo', fake_mongo)
    yield db
    test_client.drop_database("TEST_ab_test_db")
