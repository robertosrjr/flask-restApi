# -*- coding: utf-8 -*-

# Importamos as classes API e Resource
from flask_restful import Api, Resource
from apps.users.resources import UserController
from apps.users.patienceResource import PatienceController
from apps.users.doctorResource import DoctorController

# Instânciamos a API do FlaskRestful
api = Api()

def configure_api(app):

    # adicionamos na rota '/' a sua classe correspondente Index
    api.add_resource(PatienceController, '/patiences', '/patiences/<string:id>')
    api.add_resource(DoctorController, '/doctors', '/doctors/<int:id>')

    # inicializamos a api com as configurações do flask vinda por parâmetro
    api.init_app(app)