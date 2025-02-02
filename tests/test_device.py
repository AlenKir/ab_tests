import pytest
from datetime import datetime

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models import Device


def test_device_creation(patch_mongo):
    mongo = patch_mongo

    assert mongo is not None, "MongoDB connection failed!"
    assert mongo.db is not None, "MongoDB connection failed!"

    print(type(mongo))
    print(type(mongo.db))

    device_token = "test_device_123"

    Device.create(device_token)

    device = Device.get_by_token(device_token)

    assert device is not None

    print('device')
    print(device)

    assert device["id"] == device_token
    assert isinstance(device["created_at"], datetime)

    assert mongo.db.devices.count_documents({}) == 1
