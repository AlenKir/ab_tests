from datetime import datetime


def test_setup(patch_mongo):
    mongo = patch_mongo

    assert mongo is not None, "MongoDB connection failed!"
    assert mongo.db is not None, "MongoDB connection failed!"

    experiments_collection = mongo.db.experiments

    from db import DEFAULT_EXPERIMENTS as expected_experiments

    for experiment_name, data in expected_experiments.items():
        experiment = experiments_collection.find_one({"name": experiment_name})
        assert experiment is not None
        assert experiment["options"] == data["options"]
        assert isinstance(experiment["created_at"], datetime)

    assert mongo.db.experiments.count_documents({}) == 2
