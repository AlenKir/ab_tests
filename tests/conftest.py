import mongomock
import pytest

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app_with_config
from config.config import TestingConfig

from db import mongo, setup_experiments


@pytest.fixture()
def app(request):
    test_app = create_app_with_config(TestingConfig)
    with test_app.app_context():
        yield test_app


@pytest.fixture(autouse=True)
def patch_mongo(monkeypatch):
    db = mongomock.MongoClient()
    setup_experiments(db)

    def fake_mongo():
        return db

    monkeypatch.setattr('db.mongo', fake_mongo)
    return db
