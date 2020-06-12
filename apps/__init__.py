# -*- coding: utf-8 -*-

import firebase_admin

from flask import Flask
from config import config
from .api import configure_api
from firebase_admin import credentials
from firebase_admin import firestore
from flask import jsonify 

def create_app(config_name):
    app = Flask('api-users')
    app.config.from_object(config[config_name])
    configure_api(app)
    return app