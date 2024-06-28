from fastapi import FastAPI,HTTPException
from model import Customer
import json


app=FastAPI()

with open("data.json", "r") as txt:
    data_customer=json.load(txt)#cargar archivos
    customerList=[Customer(**i) for i in data_customer]##** cambia clave valor a tipo objeto , diccionario a lista 

@app.get("/Customer")
async def Consult():
    return customerList

@app.get("/Customer/{document}")
async def customerConsult(document:str) :
    for i in customerList:
        if i.DNI==document: #con punto accedo a los atributos del objeto cliente
            return i
    raise HTTPException(status_code=404, detail="Customer not found")


@app.post("/Customer",response_model=Customer)   #llega objeto cliente
async def add(customer: Customer):
    for i in customerList:
        if i.DNI==customer.DNI:
            raise HTTPException(status_code=404 , detail="That document is already in the list")
    customerList.append(customer)

    with open ("data.json","w") as txt:
        json.dump([i.dict() for i in customerList],txt, indent=4)
    return i    

@app.put("/Customer/{dni}",response_model=Customer) 
async def update(dni: str, updated_customer: Customer):
    for i, data in enumerate(customerList):
        if data.DNI == dni:
            customerList[i] = updated_customer
            with open("data.json", "w") as txt:
                json.dump([j.dict() for j in customerList], txt, indent=4)
            return updated_customer
    raise HTTPException(status_code=404, detail="Customer not found")



@app.delete("/Customer/{dni}")
async def deleteCustomer(dni: str):
    for i, customer in enumerate(customerList):
        if customer.DNI == dni:
            customerList.pop(i)
            with open("data.json", "w") as txt:
                json.dump([j.dict() for j in customerList], txt, indent=4)
            return f"The customer {customer.name} was deleted"
    raise HTTPException(status_code=404, detail="Customer not found")