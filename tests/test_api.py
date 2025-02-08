from datetime import datetime
import uuid

from models import Experiment


def generate_random_token():
    return str(uuid.uuid4())


def test_get_experiments(client):
    headers = {
        "Device-Token": generate_random_token()
    }
    response = client.get("/get_experiments", headers=headers)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"


def test_same_experiments_per_token(client):
    headers = {
        "Device-Token": generate_random_token()
    }
    response = client.get("/get_experiments", headers=headers)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    experiments_1 = response.json

    response = client.get("/get_experiments", headers=headers)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    experiments_2 = response.json

    assert experiments_1 == experiments_2, "Experiment assignments should remain the same for the device token"


def test_only_new_experiments(client):
    old_device = generate_random_token()
    headers = {
        "Device-Token": old_device
    }
    # now the device is saved and new experiments should not apply to it
    response = client.get("/get_experiments", headers=headers)

    options = {
            "left": 0.5,
            "right": 0.25,
            "center": 0.25
        }

    Experiment.create_experiment("header_text_alignment", options)

    response = client.get("/get_experiments", headers=headers)
    old_experiments = response.json

    new_device = generate_random_token()
    headers = {
        "Device-Token": new_device
    }
    # new device should have all the experiments
    response = client.get("/get_experiments", headers=headers)
    new_experiments = response.json

    assert len(new_experiments) - len(old_experiments) == 1

    assert new_experiments['header_text_alignment'] in options.keys(), \
        f"Invalid value for header_text_alignment: {new_experiments['header_text_alignment']}"
