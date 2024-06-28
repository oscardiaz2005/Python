from fastapi import FastAPI
from dictionary import data_base

app = FastAPI()

usersdict={}
usersdict=data_base()


@app.get("/")
async def first_function():
    return usersdict

@app.get("/customer/{id}")
async def search(id:str):

    for v in usersdict.values():
        if v["dni"]==id:
            return v






