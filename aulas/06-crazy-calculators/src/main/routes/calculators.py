from flask import Blueprint, jsonify, request
from src.main.factories.calculator4_factory import calculator4_factory
from src.main.factories.calculator3_factory import calculator3_factory
from src.main.factories.calculator2_factory import calculator2_factory
from src.main.factories.calculator1_factory import calculator1_factory

from src.errors.error_controller import handle_errors

calc_route_bp = Blueprint("calc_routes", __name__)

@calc_route_bp.route("/calculator/1", methods=["POST"])
def calculator1():
    try:
        calc = calculator1_factory()
        response = calc.calculate(request)

        return jsonify(response), 200
    except Exception as exception:
        error_response = handle_errors(exception)
        return jsonify(error_response["body"]), error_response["status_code"]


@calc_route_bp.route("/calculator/2", methods=["POST"])
def calculator2():
    try:
        calc = calculator2_factory()
        response = calc.calculate(request)

        return jsonify(response), 200
    except Exception as exception:
        error_response = handle_errors(exception)
        return jsonify(error_response["body"]), error_response["status_code"]

@calc_route_bp.route("/calculator/3", methods=["POST"])
def calculator_3():
    try:
        calc = calculator3_factory()
        response = calc.calculate(request)

        return jsonify(response), 200
    except Exception as exception:
        error_response = handle_errors(exception)
        return jsonify(error_response["body"]), error_response["status_code"]

@calc_route_bp.route('/calculator/4', methods=['POST'])
def calculator_4():
    try:
        calc = calculator4_factory()
        response = calc.calculate_average(request)

        return jsonify(response), 200
    except Exception as exception:
        error_response = handle_errors(exception)
        return jsonify(error_response["body"]), error_response["status_code"]