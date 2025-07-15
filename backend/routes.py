from flask import Blueprint, request, jsonify
from flask_cors import CORS
from datetime import datetime, timezone

api_v1 = Blueprint(
    'api_v1', 'api_v1', url_prefix='/api/v1')

CORS(api_v1)

@api_v1.route('/')
def api_get_default():
    return jsonify({
        "retrieved": datetime.now(timezone.utc).isoformat()
    })
