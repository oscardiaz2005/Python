import firebase_admin
from firebase_admin import credentials,firestore
from fastapi import FastAPI

app=FastAPI()

cred=credentials.Certificate('C:/Users/janet/OneDrive/Escritorio/data_base 01/proyect-01-e2c8a-firebase-adminsdk-wwjs8-b4b54dd1ed.json')
firebase_admin.initialize_app(cred)


db=firestore.client()
basedata=db.collection('Customer').get()

for i in basedata:
    print(f"{i.id}  {i.to_dict()}")

@app.get("/datafire")
async def get_data():
    basedata=db.collection('Customer').get()
    data=[{i.id:i.to_dict()} for i in basedata]  
    return data  
