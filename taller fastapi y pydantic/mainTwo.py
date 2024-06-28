from fastapi import FastAPI, HTTPException
from ModelUser import User
import json

app=FastAPI()

with open ("baseDataUsers.json" , "r") as txt:
    data_users=json.load(txt)
    list_users=[User(**i) for i in data_users]


# Ruta POST para crear un nuevo Usuario:
@app.post("/addUser")
async def add_user(new_user:User):
    if new_user.age<18:
        raise HTTPException (status_code=400,detail="The user must be at least 18 years old")
    
    for user in list_users:
        if user.id == new_user.id:
            raise HTTPException (status_code=400,detail="The user is already in the base data")
    list_users.append(new_user)
    with open ("baseDataUsers.json", "w") as txt:
        json.dump([i.dict() for i in list_users] , txt,indent=4)
    return{"msg":f"The user {new_user.id} was added"} 


# Ruta GET para obtener todos los Usuarios:
@app.get("/allUsers")
async def all_users():
    if list_users :
        return list_users
    else:
        raise HTTPException(status_code=404,detail="the base data is empty")
     

#Ruta GET para obtener un Usuario por su id   
@app.get("/userId/{findId}")  
async def user_id(findId:str):
    for user in list_users:
        if user.id == findId:
            return user
    raise HTTPException(status_code=404,detail=f"the id {findId} does not exist") 


# Ruta PUT para actualizar un Usuario existente
@app.put("/updateUser/{findId}")
async def update_user(findId:str,update_user:User):
    if update_user.age<18:
        raise HTTPException(status_code=400, detail="The user must be at least 18 years old")
    
    for i , User in enumerate(list_users):
        if User.id == findId:
            list_users[i]=update_user
            with open ("baseDataUsers.json","w") as txt:
                json.dump([i.dict() for i in list_users],txt,indent=4)
                return {"msg":f"the user {findId} was updated"} 
    raise HTTPException(status_code=404,detail=f"the id {findId} does not exist")    


# Ruta DELETE para eliminar un Usuario:       
@app.delete("/deleteUser/{findId}")  
async def delete_user(findId:str):
    for user in list_users:
        if user.id == findId:
            list_users.remove(user)
        with open ("baseDataUsers.json","w") as txt:
            json.dump([i.dict() for i in list_users] , txt,indent=4)
            return {"msg":f"the user {findId} was deleted"} 

    raise HTTPException(status_code=404,detail=f"the id {findId} does not exist") 
