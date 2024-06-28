import firebase_admin
from firebase_admin import firestore,credentials
from fastapi import FastAPI,HTTPException

app=FastAPI()

credential=firebase_admin.credentials.Certificate("C:/Users/janet/OneDrive/Escritorio/taller firestore_fastapi 01/keys/customer-management-d998a-firebase-adminsdk-71l7h-03f29289ea.json")

firebase_admin.initialize_app(credential)

client=firestore.client()

@app.get("/order")
async def get_orders():
    orders=[]
    data_base_order=client.collection(" order").get()
    for document in data_base_order:
        data=document.to_dict()
        orders.append( f" {document.id} : {data}") 

    if orders:    
        return orders  
    else:
        raise HTTPException (status_code=404,detail="there are not any order in the data base")
    

@app.get("/order_customer/{customer_id}")
async def get_orders_customer(customer_id:str):
    data_base_order=client.collection(" order").get()
    orders=[]
    for document in data_base_order:
        data=document.to_dict()
        if data.get("customer_id") == customer_id :
            orders.append(data)

    if orders:    
        return {f"{customer_id}'s orders :" : orders}
    else:
        raise HTTPException (status_code=404,detail=f"the customer {customer_id} does not has any order")            


@app.get("/personal")
async def get_personal_client():
    data_base_customer=client.collection("customer").get()
    customers=[]
    for document in data_base_customer:
        data=document.to_dict()
        if data.get("type") == "personal" :
            customers.append(data)    
    if customers:    
        return {" personal customers  :" : customers}
    else:
        raise HTTPException (status_code=404,detail=f"there are not  any personal customer")  


@app.get("/corporate")
async def get_corporate_client():
    data_base_customer=client.collection("customer").get()
    customers=[]
    for document in data_base_customer:
        data=document.to_dict()
        if data.get("type") == "corporate" :
            customers.append(data)    
    if customers:    
        return {" corporate customers  :" : customers}
    else:
        raise HTTPException (status_code=404,detail=f"there are not  any corporate customer")                  


@app.get("/product")
async def get_product():
    data_base_product=client.collection("product").get()
    products=[]
    for document in data_base_product:
        data=document.to_dict()
        products.append(data)    
    if products:    
        return {f"products  : {products}"}
    else:
        raise HTTPException (status_code=404,detail=f"there are not  any products")  
    


 
@app.get("/seller_customer/{seller_id}")
async def get_seller_customer(seller_id: str):
    base_data_seller = client.collection("seller").get()
    base_data_customer = client.collection("customer").get()

    seller_data = None
    for document in base_data_seller:
        data = document.to_dict()
        if data.get("id") == seller_id:
            seller_data = data
            break

    if seller_data:
        for document in base_data_customer:
            data_customer = document.to_dict()
            if data_customer.get("id") == seller_data.get("customer_id") :
                return {f"{seller_data.get('id')}, {seller_data.get("name")}'s customer": data_customer.get("name")}
        return f"Customer not found for the seller : {seller_data.get('id')}"
    else:
        raise HTTPException(status_code=404, detail="seller not found")


@app.get("/customer")
async def get_custumer():
    data_base_customer=client.collection("customer").get()
    customers=[]
    for document in data_base_customer:
        data=document.to_dict()
        customers.append(data)    
    if customers:    
        return {f"customers  : {customers}"}
    else:
        raise HTTPException (status_code=404,detail=f"there are not  any customer") 
    
    
@app.get("/seller")
async def get_seller():
    data_base_seller=client.collection("seller").get()
    sellers=[]
    for document in data_base_seller:
        data=document.to_dict()
        sellers.append(data)    
    if sellers:    
        return {f"sellers  : {sellers}"}
    else:
        raise HTTPException (status_code=404,detail=f"there are not  any seller")     



    





    

        


