# -*- coding: utf-8 -*-

# Importamos as classes API e Resource
from flask_restful import Api, Resource
from apps.users.resources import UserController

# Instânciamos a API do FlaskRestful
api = Api()

def configure_api(app):

    # adicionamos na rota '/' a sua classe correspondente Index
    api.add_resource(UserController, '/users', '/users/<int:id>')

    # inicializamos a api com as configurações do flask vinda por parâmetro
    api.init_app(app)