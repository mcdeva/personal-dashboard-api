import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('personal-dashboard-firebase-adminsdk.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

def read_collection_login_game():
    doc_ref = db.collection('login_game').document('20211206')
    docs = doc_ref.get()
    return docs.to_dict()
