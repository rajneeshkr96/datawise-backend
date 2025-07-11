from flask import Blueprint,jsonify


home_bp = Blueprint('home', __name__)

@home_bp.route('/', methods=['GET'])
def home():
    return jsonify({"message": "API is running"}), 200
