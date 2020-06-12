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
            return self.repository.find_all()
        except ValueError as error:
            print('PatienceService:post::erro...'+str(error))
            raise        