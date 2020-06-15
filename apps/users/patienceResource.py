from flask import request
from flask_restful import Resource
from apps.users.schemas import UserSchema
from apps.users.service import PatienceService

class PatienceController(Resource):

    service = PatienceService()
    def get(self, *args, **kwargs):

        id = kwargs.get('id', None)
        if id == None:
            print('resource::userController::get::findAll')
            users =  self.service.findAll()
            print('resource::userController::get::findAll::qtde::'+ str(len(users)))
            print(users)
            return users
        else:
            print('resource::userController::get::findById::'+str(id))
            return self.service.findById(id), 200

    def post(self, *args, **kwargs):

        print('resource::userController::post::'+str(request.get_json()))
        req_data = request.get_json() or None        
        print(type(req_data))
        result = UserSchema().load(req_data)
        response = self.service.post(result)
        return response, 201

    def put(self, *args, **kwargs):

        print('resource::userController::put::'+str(request.get_json()))
        req_data = request.get_json() or None   
        result = UserSchema().load(req_data)
        response = self.service.put(result)     
        return req_data, 200

    def delete(self, id):

        print('resource::userController::delete::'+str(id))
        self.service.delete(id)
        return None, 200    