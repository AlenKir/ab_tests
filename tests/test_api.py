import math
import uuid

import pytest

from models import Experiment, Device


def generate_random_token():
    return str(uuid.uuid4())


def test_get_experiments(client):
    headers = {
        "Device-Token": generate_random_token()
    }
    response = client.get("/get_experiments", headers=headers)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"


def test_same_experiments_per_device(client):
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

    assert old_experiments.keys() <= new_experiments.keys(), f"Old experiments should be included"

    assert new_experiments['header_text_alignment'] in options.keys(), \
        f"Invalid value for header_text_alignment: {new_experiments['header_text_alignment']}"


@pytest.mark.usefixtures("clean_db")
def test_distribution_db(patch_mongo, client):
    color_assignments = []
    total_count = 600
    distribution = 1/3
    expected_count = total_count * distribution
    sigma = math.sqrt(total_count * distribution * (1 - distribution))
    z_score = 2.576
    lower_bound = expected_count - z_score * sigma
    upper_bound = expected_count + z_score * sigma

    for i in range(total_count):
        headers = {
            "Device-Token": generate_random_token()
        }
        response = client.get("/get_experiments", headers=headers)
        experiments = response.json
        assert "button_color" in experiments
        color_assignments.append(experiments["button_color"])

    unique_colors = set(color_assignments)
    assert len(unique_colors) == 3
    color_counts = {color: 0 for color in unique_colors}

    for color in color_assignments:
        color_counts[color] += 1

    for color in unique_colors:
        count = color_counts[color]
        assert lower_bound <= count <= upper_bound, f"Color {color} was assigned {count} times, expected {lower_bound, upper_bound}"
