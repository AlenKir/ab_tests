from flask import Blueprint, jsonify, request
from services.experiments import ExperimentService
from services.statistics import StatisticsService

ab_routes = Blueprint('ab_routes', __name__)


@ab_routes.route('/get_experiments', methods=['GET'])
def get_experiments():
    device_token = request.headers.get('Device-Token')

    if not device_token:
        return jsonify({"error": "Device-Token header is required"}), 400

    experiments_data = ExperimentService.assign_experiment(device_token)
    return jsonify(experiments_data)


@ab_routes.route('/statistics', methods=['GET'])
def statistics():
    stats = StatisticsService.get_statistics()
    return jsonify(stats)
