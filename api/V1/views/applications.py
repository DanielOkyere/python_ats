#!/usr/bin/python3
"""Objects for handling applicationss in RESTFul API"""
from models.application import Applications
from models import storage

from api.V1.views import app_views
from flask import jsonify, make_response, request, abort


@app_views.route('/applications', methods=['GET'], strict_slashes=False)
def get_applications():
    """
    Retrieve the list of all applications objects or a specific application
    """
    all_applications = storage.all(Applications).values()
    list_applications = []
    for application in all_applications:
        list_applications.append(application.to_dict())
    return make_response(jsonify(list_applications))

@app_views.route('/applications/<application_id>', methods=['GET'], strict_slashes=False)
def get_application(application_id):
    """ Retrieve a application"""
    application = storage.get(Applications, application_id)
    if not application:
        abort(404)
        
    return make_response(jsonify(application.to_dict()))
    

@app_views.route('/applications/<application_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_application(application_id):
    """
    Deletes a application object
    """
    
    application = storage.get(Applications, application_id)
    
    if not application:
        abort(404)
        
    storage.delete(application)
    storage.save()
    
    return make_response(jsonify({}), 200)


@app_views.route('/applications', methods=['POST'], strict_slashes=False)
def post_application():
    """Creates application"""
    if not request.get_json():
        abort(400, description="Not a json")
        
    data = request.get_json()
    instance = Applications(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/applications/<application_id>', methods=['PUT'], strict_slashes=False)
def put_application(application_id):
    """
    Update application
    """
    application = storage.get(Applications, application_id)
    
    if not application:
        abort(404)
        
    if not request.get_json():
        abort(400, description="Not a json")
        
    ignore = ['id', 'email', 'created_at', 'updated_at']
    
    data = request.get_json()
    for k, v in data.items():
        if k not in ignore:
            setattr(application, k, v)
    storage.save()
    return make_response(jsonify(application.to_dict()), 200)