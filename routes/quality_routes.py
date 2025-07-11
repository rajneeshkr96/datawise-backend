from flask import Blueprint, request, jsonify
from services import  quality_log_service
from utils.validation import  QualityLogSchema
from marshmallow import ValidationError

quality_bp = Blueprint('quality', __name__)


@quality_bp.route('/datasets/<id>/quality-1', methods=['POST'])
def add_quality_log(id):
    """
    Add a quality log for a dataset
    ---
    tags:
      - Quality Logs
    parameters:
      - name: id
        in: path
        type: string
        required: true
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              status:
                type: string
              comment:
                type: string
    responses:
      201:
        description: Quality log created
      400:
        description: Validation error
    """
    try:
        data = QualityLogSchema().load(request.json)
        log_id = quality_log_service.add_quality_log(id, data)
        return jsonify({"log_id": log_id}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400

@quality_bp.route('/datasets/<id>/quality-1', methods=['GET'])
def get_quality_logs(id):
    """
    Retrieve all quality logs for a dataset
    ---
    tags:
      - Quality Logs
    parameters:
      - name: id
        in: path
        type: string
        required: true
    responses:
      200:
        description: List of quality logs
    """
    logs = quality_log_service.get_quality_logs(id)
    return jsonify(logs), 200
