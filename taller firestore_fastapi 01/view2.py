import firebase_admin
from firebase_admin import credentials,firestore
from fastapi import FastAPI,HTTPException

app=FastAPI()

credential=firebase_admin.credentials.Certificate("C:/Users/janet/OneDrive/Escritorio/taller firestore_fastapi 01/keys/bird-feeding-control-firebase-adminsdk-ijpa9-f6134ca433.json")

firebase_admin.initialize_app(credential)

client=firestore.client()

#show batch by id
@app.get("/batch/{batch_id}")
async def get_lote(batch_id: str):
    base_data = client.collection("Batch").get()
    for document in base_data:
        if document.id == batch_id:
            return document.to_dict()
    raise HTTPException (status_code=404,detail="batch not found")    
        
        
#show batch's bird
@app.get("/batch_bird/{batch_id}")
async def get_aves_by_lote(batch_id: str):
    base_data=client.collection("Bird").get()
    birds=[]
    for document in base_data:
        data=document.to_dict()
        if data.get("batch_id") == batch_id :
            birds.append(data)

    if birds :
        return {f"Birds_in_{batch_id}" : birds} 
    else:
        raise HTTPException(status_code=404 ,detail=f"there are not birds in the batch {batch_id}")     
    
      

#show  feeding control by id 
@app.get("/feeding_control/{control_id}")
async def get_control(control_id:str):
    base_data = client.collection("feeding_control").get()
    for document in base_data:
        if document.id == control_id:
            return document.to_dict()
    raise HTTPException (status_code=404,detail="feeding control not found")   


#show bird by id
@app.get("/bird_id/{bird_id}")
async def get_bird(bird_id:str):
    base_data = client.collection("Bird").get()
    for document in base_data:
        if document.id == bird_id:
            return document.to_dict()
    raise HTTPException (status_code=404,detail="bird not found")     


#show food bird 
@app.get("/bird_food/{bird_id}")
async def get_bird_food(bird_id: str):
    base_data_bird = client.collection("Bird").get()
    base_data_food = client.collection("feeding_control").get()

    bird_data = None
    for document in base_data_bird:
        data = document.to_dict()
        if document.id == bird_id:
            bird_data = data
            break

    if bird_data:
        for document in base_data_food:
            data_food = document.to_dict()
            if data_food.get("batch_id") == bird_data.get("batch_id") and data_food.get("stage") == bird_data.get("status"):
                return {f"Food for the bird {bird_data.get('id')}": data_food.get("food_list")}
        return f"Food not found for the bird : {bird_data.get('id')}"
    else:
        raise HTTPException(status_code=404, detail="Bird not found")

      
            







    




     

