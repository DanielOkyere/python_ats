#!/usr/bin/python3
""" Blueprint for API """
from flask import Blueprint

app_views = Blueprint('ats', __name__, url_prefix='/api/v1')

from api.V1.views.index import *
from api.V1.views.users import * 