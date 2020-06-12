# -*- coding: utf-8 -*-

# Python
from os import getenv
from datetime import timedelta

class Config:
    SECRET_KEY = getenv('SECRET_KEY') or 'uma string randômica e gigante'
    APP_PORT = int(getenv('APP_PORT'))
    DEBUG = eval(getenv('DEBUG').title())
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(
        minutes=int(getenv('JWT_ACCESS_TOKEN_EXPIRES'))
    )
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(
        days=int(getenv('JWT_REFRESH_TOKEN_EXPIRES'))
    )

class DevelopmentConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}