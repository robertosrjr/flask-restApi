from apps.users.repository import PatienceRepository

class PatienceService():

    repository = PatienceRepository()
    def post(self, object):

        try:
            print('PatienceService:post::Salvando...')
            return self.repository.post(object)
        except ValueError as error:
            print('PatienceService:post::erro...'+str(error))
            raise

    def put(self, object):

        try:
            print('PatienceService:put::Atualizando...')
            return self.repository.put(object)
        except ValueError as error:
            print('PatienceService:put::erro...'+str(error))
            raise    

    def findById(self, id):

        try:
            print('PatienceService:findById::'+str(id))
            return self.repository.find_by_id(id)
        except ValueError as error:
            print('PatienceService:post::erro...'+str(error))
            raise 

    def findAll(self):

        try:
            print('PatienceService:findById::')
            users = self.repository.find_all()
            print('PatienceService:findById::qtde::' + str(len(users)))
            return users
        except ValueError as error:
            print('PatienceService:post::erro...'+str(error))
            raise

    def delete(self, id):

        print('PatienceService:delete::'+id)
        try:
            self.repository.delete(id)
        except ValueError as error:
            print('PatienceService:delete::erro...'+str(error))
            raise
