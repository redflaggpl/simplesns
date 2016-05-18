from app import app, jsonify
from flask.ext.pymongo import PyMongo
import time

mongo = PyMongo(app)

@app.route('/api/v1/notifications', methods=['GET'])
def get_notifications():
    currentDate = (time.strftime("%H:%M:%S")) 
    return jsonify(mongo.db.notifications.find({'sent': False}))
