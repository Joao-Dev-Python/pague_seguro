import firebase_admin
from firebase_admin import credentials,firestore
import os




class DB:
    def __init__(self):
        self.__path = os.path.dirname(os.path.realpath(__file__))
        self.path = os.path.join(self.__path,"pixapi.json")
        self.cred = credentials.Certificate(self.path)
        firebase_admin.initialize_app(self.cred)
        
    def update(self,id,field):
        database = firestore.client()
        col_ref = database.collection("Orders")
        doc = col_ref.document(id)
        doc.update(field)

