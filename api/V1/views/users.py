#!/usr/bin/python3
"""Objects for handling users in RESTFul API"""
from models.user import User
from models import storage

from api.V1.views import app_views
from flask import jsonify, make_response, request, abort


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    """
    Retrieve the list of all user objects or a specific user
    """
    all_users = storage.all(User).values()
    list_users = []
    for user in all_users:
        list_users.append(user.to_dict())
    return make_response(jsonify(list_users))

@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """ Retrieve a user"""
    user = storage.get(User, user_id)
    if not user:
        abort(404)
        
    return make_response(jsonify(user.to_dict()))
    

@app_views.route('/users/<user_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_user(user_id):
    """
    Deletes a user object
    """
    
    user = storage.get(User, user_id)
    
    if not user:
        abort(404)
        
    storage.delete(user)
    storage.save()
    
    return make_response(jsonify({}), 200)


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def post_user():
    """Creates user"""
    if not request.get_json():
        abort(400, description="Not a json")
        
    data = request.get_json()
    instance = User(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def put_user(user_id):
    """
    Update User
    """
    user = storage.get(User, user_id)
    
    if not user:
        abort(404)
        
    if not request.get_json():
        abort(400, description="Not a json")
        
    ignore = ['id', 'email', 'created_at', 'updated_at']
    
    data = request.get_json()
    for k, v in data.items():
        if k not in ignore:
            setattr(user, k, v)
    storage.save()
    return make_response(jsonify(user.to_dict()), 200)