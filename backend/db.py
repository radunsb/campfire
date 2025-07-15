from flask import current_app, g, session
from werkzeug.local import LocalProxy
from flask_pymongo import PyMongo

def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = PyMongo(current_app).db       
    return db

db = LocalProxy(get_db)

def get_stories():
    try:
        return list(db.Stories.find({}))
    except Exception as e:
        return e
    
def find_max_story_id():
    try:
        stories = list(db.Stories.find({}))
        if(len(stories) == 0):
            return -1
        return stories[len(stories)-1]['_id']
    except Exception as e:
        return e

def push_new_story(user_id, story_contents):
    try:
        story_id = find_max_story_id() + 1
        story_object = {"_id":story_id, "user_id":user_id, "contents":story_contents}
        stories = db.get_collection("Stories")
        stories.insert_one(story_object)
        return story_id
    except Exception as e:
        return e
