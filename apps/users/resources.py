
from flask import request
from flask_restful import Resource

class UserController(Resource):

    def get(self, *args, **kwargs):

        id = kwargs.get('id', None)
        if id == None:
            print('resource::userController::get::id::None')
        else:
            print('resource::userController::get::id::'+str(id))

        return {'resource': 'userController::get::'}, 200    


    def post(self, *args, **kwargs):

        print('resource::userController::post::'+str(request.get_json()))
        req_data = request.get_json() or None        
        return req_data, 201

    def put(self, *args, **kwargs):

        print('resource::userController::put::'+str(request.get_json()))
        req_data = request.get_json() or None        
        return req_data, 200

    def delete(self, id):

        print('resource::userController::delete::'+str(id))
        return {'id': id}, 200    