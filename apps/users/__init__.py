import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

def get_firestore_client():

    print("init_config_firestore...")
    try:

        cred = credentials.Certificate('static/data-base-teste-277100-8a0d28ccf452.json')
        firebase_admin.initialize_app(cred)
        db = firestore.client()
        return db
    except ValueError as error:
        print("erro ao init_config_firestore." + str(error))