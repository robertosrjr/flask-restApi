
import firebase_admin
import uuid
import google.cloud.exceptions
from apps.users import get_firestore_client
from google.cloud import firestore
from firebase_admin import firestore

class PatienceRepository():

    def __init__(self):
        firebase_admin.initialize_app()

    def post(self, object):

        try:
            print('PatienceRepository:post::Salvando...')
            self.get_check_email_exists(object.get('email'))
            db = firestore.client()
            id = uuid.uuid4()
            doc_ref = db.collection(u'patiences').document(str(id))
            doc_ref.set({
                u'id': str(id),
                u'first': object.get('first_name'),
                u'last': object.get('last_name'),
                u'email': object.get('email'),
                u'cpf': object.get('cpf')
            })
            print('PatienceRepository:post::salvo...')
            return doc_ref.get().to_dict()
        except ValueError as error:
            print('PatienceRepository:post::erro...'+ str(error))
            raise

    def put(self, object):

        try:
            print('PatienceRepository:put::Atualizando...'+object.get('id'))
            db = firestore.client()
            doc_ref = db.collection(u'patiences').document(object.get('id'))
            doc = doc_ref.get()

            doc_ref.update({
                u'first': object.get('first_name'),
                u'last': object.get('last_name'),
                u'email': object.get('email'),
                u'cpf': object.get('cpf')
            })
            print('PatienceRepository:put::salvo...')
            return doc_ref.get().to_dict()
        except google.cloud.exceptions.NotFound:

            print(u'Identificador não encontrado.')    
            raise ValueError('Identificador {} não encontrado.'.format(object.get('id')))
        except ValueError as error:

            print('PatienceRepository:put::erro...'+ str(error))
            raise


    def get_check_email_exists(self, email):

        try:
            print('PatienceRepository:get_check_email_exists::')
            db = firestore.client()
            docs = db.collection(u'patiences').where(u'email', u'==', email).stream()
            my_dict = { el.id: el.to_dict() for el in docs }
            if len(my_dict) > 0 :                
                raise ValueError('O E-mail {} já está cadastrado.'.format(email))

        except google.cloud.exceptions.NotFound:
            print('PatienceRepository:get_check_email_exists::NotFound...')
            return None
        except ValueError as error:
            raise

    def find_by_id(self, id):

        print('PatienceRepository:get_by_id::'+id)
        db = firestore.client()
        doc = db.collection(u'patiences').document(id)
        print('---------->'+str(doc.get().to_dict()))
        return doc.get().to_dict()

    def find_all(self):

        users = []
        print('PatienceRepository:findAll::')
        db = firestore.client()
        docs = db.collection(u'patiences').stream()

        for doc in docs:
            users.append(doc.to_dict())

        print('PatienceRepository:findAll::qtde::'+ str(len(users)))
        return users
    
    def delete(self, id):
        print('PatienceRepository:delete::'+id)
        db = firestore.client()
        db.collection(u'patiences').document(id).delete()