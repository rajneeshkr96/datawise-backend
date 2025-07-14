from flask import Blueprint, request, jsonify
from services import dataset_service
from utils.validation import DatasetSchema
from marshmallow import ValidationError
from utils.json_encoder import serialize_doc, serialize_list

dataset_bp = Blueprint('datasets', __name__)

@dataset_bp.route('/datasets', methods=['POST'])
def create_dataset():
    """
    Create a new dataset
    ---
    tags:
      - Datasets
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              name:
                type: string
                example: "Climate Stats"
              owner:
                type: string
                example: "raju"
              description:
                type: string
                example: "This dataset contains annual climate stats."
              tags:
                type: array
                items:
                  type: string
                example: ["climate", "weather", "2025"]
            required:
              - name
              - owner
              - description
              - tags
    responses:
      201:
        description: Dataset created successfully
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  example: "60f6cbbcf3c531a2b7d6e8a9"
      400:
        description: Validation error
    """
    try:
        data = DatasetSchema().load(request.json)
        dataset_id = dataset_service.create_dataset(data)
        return jsonify({"id": dataset_id}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400

@dataset_bp.route('/datasets', methods=['GET'])
def list_datasets():
    """
    List all datasets
    ---
    tags:
      - Datasets
    parameters:
      - name: owner
        in: query
        type: string
        required: false
      - name: tag
        in: query
        type: string
        required: false
    responses:
      200:
        description: List of datasets
    """
    owner = request.args.get("owner")
    tag = request.args.get("tag")
    limit = request.args.get("limit")
    if limit is not None:
        try:
            limit = int(limit)
        except ValueError:
            return {"error": "limit must be an integer"}, 400
    
    datasets = dataset_service.list_datasets(owner, tag,limit)
    return jsonify(serialize_list(datasets)), 200

@dataset_bp.route('/datasets/<id>', methods=['GET'])
def get_dataset(id):
    """
    Get a dataset by ID
    ---
    tags:
      - Datasets
    parameters:
      - name: id
        in: path
        type: string
        required: true
        description: The ID of the dataset
    responses:
      200:
        description: Dataset found
        schema:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
            description:
              type: string
      404:
        description: Dataset not found
    """
    dataset = dataset_service.get_dataset(id)
    if not dataset:
        return jsonify({"error": "Dataset not found"}), 404
    return jsonify(serialize_doc(dataset)), 200

@dataset_bp.route('/datasets/<id>', methods=['PUT'])
def update_dataset(id):
    """
    Update a dataset by ID
    ---
    tags:
      - Datasets
    parameters:
      - name: id
        in: path
        type: string
        required: true
        description: The ID of the dataset
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            description:
              type: string
          required:
            - name
    responses:
      200:
        description: Dataset updated successfully
      400:
        description: Update failed or invalid input
    """
    success = dataset_service.update_dataset(id, request.json)
    if not success:
        return jsonify({"error": "Update failed"}), 400
    return jsonify({"message": "Dataset updated"}), 200

@dataset_bp.route('/datasets/<id>', methods=['DELETE'])
def soft_delete_dataset(id):
    """
    Soft delete a dataset by ID
    ---
    tags:
      - Datasets
    parameters:
      - name: id
        in: path
        type: string
        required: true
        description: The ID of the dataset
    responses:
      200:
        description: Dataset soft deleted successfully
      400:
        description: Delete failed
    """
    success = dataset_service.soft_delete_dataset(id)
    if not success:
        return jsonify({"error": "Delete failed"}), 400
    return jsonify({"message": "Dataset soft deleted"}), 200

