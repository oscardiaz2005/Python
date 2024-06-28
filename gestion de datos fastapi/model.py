from pydantic import BaseModel

class Customer(BaseModel):
    DNI:str
    name:str
    lastName:str
    email:str
    phone:str
    age:str