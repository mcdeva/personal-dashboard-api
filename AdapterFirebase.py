import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import datetime

cred = credentials.Certificate('personal-dashboard-firebase-adminsdk.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

def read_collection_environment():
    doc_ref = db.collection('status_environment').document('environment1')
    docs = doc_ref.get()
    environment_data: dict = docs.to_dict()
    sorted_environment_data: dict = dict(sorted(environment_data.items(), key=lambda item: item[1], reverse=True))
    environment_data_dict: dict = get_format_datetime(sorted_environment_data)
    return environment_data_dict

def get_format_datetime(data_collection_dict: dict) -> dict:
    new_data_dict: dict = {}
    for detail in data_collection_dict:
        if not data_collection_dict[detail] == 'N/A':
            date: str = data_collection_dict[detail]
            date_format = datetime(int(date[0:4]), int(date[4:6]), int(date[6:8]),
                                    int(date[9:11]), int(date[11:13]), int(date[13:15]))
            date_format: str = f'{date_format:%d %B %Y} Time {date_format:%H:%M:%S}'
        else:
            date_format: str = data_collection_dict[detail]
        new_data_dict[detail] = date_format
    return new_data_dict

def get_current_format_datetime() -> str:
    current_datetime = datetime.now()
    format_datetime: str = f'{current_datetime:%Y%m%d}-{current_datetime:%H%M%S}'
    return format_datetime
