#!/usr/bin/python3
""" Api For ATS APPLICATION"""

from models import storage
from os import environ
from flask import Flask, render_template, make_response, jsonify
from flask_cors import CORS
from api.V1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

@app.teardown_request
def close_db(error):
    """Close storage"""
    storage.close()
    
    
@app.errorhandler(404)
def not_found(error):
    """404 Error"""
    return make_response(jsonify({'error':'Not Found'}), 404)

if __name__ == "__main__":
    """Main Function"""
    host = environ.get('ATS_API_HOST')
    port = environ.get('ATS_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = 3001
        
    app.run(host=host, port=port, threaded=True)

