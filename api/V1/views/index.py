#!/usr/bin/python3

from models.application import Applications
from models.role import Role
from models.user import User
from models import storage
from api.V1.views import app_views
from flask import make_response, jsonify

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of API """
    return make_response(jsonify({"status": "OK"}))

@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def number_object():
    """Retrieves the number of each object by type"""
    classes = [Role, User, Applications]
    names = ["role", "users", "applications"]
    
    num_objs = {}
    for i in range(len(classes)):
        num_objs[names[i]] = storage.count(classes[i])
        
    return make_response(jsonify(num_objs))