import firebase_admin
from firebase_admin import firestore,credentials
from fastapi import FastAPI,HTTPException

app=FastAPI()

#crear credenciales para poder acceder al proyecto
credential=credentials.Certificate("C:/Users/janet/OneDrive/Escritorio/taller firestore_fastapi 01/Keys/reserva-vuelos-50717-firebase-adminsdk-sp6vi-8eeb1993f7.json")
#inicializar la app
firebase_admin.initialize_app(credential)
#crear un cliente para poder acceder a las colecciones
client=firestore.client()


# Flight for time
@app.get("/time/{origin_city}/{destination_city}")
async def get_flight_time(origin_city: str, destination_city: str) :
    # Obtener los datos de la colección
    data_base = client.collection("Flight").get()
    flights = []
    for document in data_base:
        #convierto cada documento en un diccionario para poder acceder a los datos con el getnm
        data = document.to_dict()
        if data.get("origin") == origin_city and data.get("destination") == destination_city:
            #añado un diccionario a la lista / se ve mejor
            flights.append({
                "airline": data.get("airline"),
                "origin city": data.get("origin"),
                "destination city": data.get("destination"),
                "time": data.get("time")
            })
    if flights:        
        return {"flights according to the time ": flights}
    else:
        raise HTTPException(status_code=404 ,detail=f"There are no flights available from {origin_city} to {destination_city}")
        


@app.get("/fare/{origin_city}/{destination_city}")
async def get_flight_fare(origin_city:str,destination_city:str):
    data_base=client.collection("Flight").get()
    flights=[]
    for document in  data_base:
        data=document.to_dict()
        if data.get("origin")==origin_city and data.get("destination")==destination_city:
            flights.append({
                "Airline":data.get("airline"),
                "Origin city":data.get("origin"),
                "Destination city":data.get("destination"),
                "Fare":data.get("fare")
            })
    if flights:
        return {"flights according to the fare " : flights}        
    else:
        raise HTTPException(status_code=404 ,detail=f"There are no flights available from {origin_city} to {destination_city}")
    


@app.get("/id/{id_find}")
async def flight_id(id_find:str):
    data_base=client.collection("Flight").get()
    flight_found=[]
    for document in data_base:
        data=document.to_dict()
        if document.id==id_find:
            flight_found.append({
            "Airline":data.get("airline"),
            "Origin city":data.get("origin"),
            "Destination city":data.get("destination"),
            "Time":data.get("time"),
            "Fare":data.get("fare")
            })
            break
    if not flight_found:
        raise HTTPException(status_code=404, detail=f"the flight with th id {id_find} does not exist")
    return {f"Flight {id_find}:" : flight_found}    



        
            








