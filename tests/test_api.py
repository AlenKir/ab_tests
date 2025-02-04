import uuid


def generate_random_token():
    return str(uuid.uuid4())


def test_get_experiments(client):
    headers = {
        "Device-Token": generate_random_token()
    }
    response = client.get("/get_experiments", headers=headers)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
