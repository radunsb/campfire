from flask import Blueprint, request, jsonify
from flask_cors import CORS
from datetime import datetime, timezone
from db import get_stories, push_new_story

api_v1 = Blueprint(
    'api_v1', 'api_v1', url_prefix='/api/v1')

CORS(api_v1)

@api_v1.route('/')
def api_get_default():
    return jsonify({
        "retrieved": datetime.now(timezone.utc).isoformat()
    })

@api_v1.route('/stories')
def api_get_stories():
    stories = get_stories()
    return jsonify({
        "retrieved": datetime.now(timezone.utc).isoformat(),
        "count": len(stories),
        "stories": stories
    })

@api_v1.route('/stories/new/<int:user_id>', methods=['GET', 'POST'])
def api_post_new_story(user_id):
    story = request.get_json()
    story_id = push_new_story(user_id, story['data']['contents'])
    return jsonify({
        "retrieved": datetime.now(timezone.utc).isoformat(),
		"story_id": story_id
    })