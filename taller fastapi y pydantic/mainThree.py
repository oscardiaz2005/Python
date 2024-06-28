from fastapi import FastAPI,HTTPException
import json
from mainOne import product_list
from mainTwo import list_users
from ModelOrder import order

app=FastAPI()

with open("orders.json" , "r") as txt:
    orders_data=json.load(txt)
    list_orders=[order(**i) for i in orders_data]


# Ruta POST para crear una nueva Orden
@app.post("/addOrder")
async def add_order(new_order:order):
    exist_id_product=True
    exist_id_user=False
    #verificar si el id no existe
    for order in list_orders:
        if order.id == new_order.id :
            raise HTTPException (status_code=400 , detail="the order is already in the base data")

    #verificar si el id del usuario existe en la lista de usuarios   
    for user in list_users:
        if user.id==new_order.id_usuario:
            exist_id_user=True
            break

    #verificar si los id de los productos existen en la lista de productos   
    for id_product in new_order.lista_productos:
        if id_product not in [product.id for product in product_list]:
            exist_id_product = False
            break


    if not  exist_id_user :                  
        raise HTTPException (status_code=400 , detail="the id_user does not exist in the user's base data")
    
    if not exist_id_product :                  
        raise HTTPException (status_code=400 , detail="you have an invalid id in your product list") 
    
    #calcular total
    total_products=0
    for id_product in new_order.lista_productos:
        for product in product_list:
            if product.id==id_product:
                total_products+=product.price

    new_order.total=total_products

    list_orders.append(new_order)

    with open("orders.json" , "w") as txt:
        json.dump([i.dict() for i in list_orders] , txt , indent=4)
        return {"" : f"the product {new_order.id} was added"}            


# Ruta GET para obtener todas las Ordenes
@app.get ("/allOrders")
async def all_orders():
    if not list_orders:
        raise HTTPException (status_code=404 , detail="the order's base data is empty")
    else:
        return list_orders
    

#Ruta GET para obtener una Orden por su id
@app.get ("/orderId/{find_id}")
async def order_id(find_id:str):
    for order in list_orders:
        if order.id==find_id:
            return order
    raise HTTPException (status_code=404,detail= f"the id {find_id} does not exist")    


# Ruta PUT para actualizar una Orden existente
@app.put ("/updateOrder/{find_id}")
async def update_order(find_id:str,updateOrder:order):
    exist_order=False
    exist_id_product=True
    exist_id_user=False
    index=0
    for i,order in enumerate(list_orders):
        if order.id == find_id :
            exist_order=True
            index=i    
            break

    if not exist_order:
        raise HTTPException (status_code=404,detail=f"the id {find_id} does not exist")
    else:
        #verificar si el id del usuario existe en la lista de usuarios   
        for user in list_users:
            if user.id==updateOrder.id_usuario:
                exist_id_user=True
                break
            #verificar si los id de los productos existen en la lista de productos   
        for id_product in updateOrder.lista_productos:
            if id_product not in [product.id for product in product_list]:
                exist_id_product = False
                break    

        if not exist_id_user:                  
            raise HTTPException (status_code=400 , detail="the id_user does not exist in the user's base data")
    
        if not exist_id_product:                  
            raise HTTPException (status_code=400 , detail="you have an invalid id in your product list") 
    
        #calcular total
        total_products=0
        for id_product in updateOrder.lista_productos:
            for product in product_list:
                if product.id==id_product:
                    total_products+=product.price

        updateOrder.total=total_products    

        list_orders[index]=updateOrder

        with open("orders.json" , "w") as txt:
            json.dump([i.dict() for i in list_orders] , txt , indent=4)
            return {"" : f"the product {find_id} was updated"}  
        
        
        
# Ruta DELETE para eliminar una Orden:
@app.delete ("/deleteOrder/{find_id}")
async def delete_order(find_id:str):
    for order in list_orders:
        if order.id==find_id:
            list_orders.remove(order)
            with open("orders.json" , "w") as txt:
                json.dump([i.dict() for i in list_orders] , txt , indent=4)
                return f"the order {find_id} was deleted"
                
    raise HTTPException (status_code=404,detail=f"the id {find_id} does not exist") 
    


#Ruta GET para obtener todas las Ordenes de un Usuario:
@app.get ("/orderUserId/{find_user_id}")
async def order_id(find_user_id:str):
    all=[]
    for order in list_orders:
        if order.id_usuario==find_user_id:
            all.append(order)
    if all :
        return all       
    else:
        raise HTTPException(status_code=404,detail=f"there are no orders with the user_id {find_user_id}")
    

# Ruta GET para obtener el total gastado por un Usuario
@app.get ("/totalUserId/{find_user_id}")
async def total_id(find_user_id:str):
    total=0
    for order in list_orders:
        if order.id_usuario==find_user_id:
            total+=order.total
    if total>0:
        return f"The user {find_user_id}'s total is {total}"        
    else:
        raise HTTPException(status_code=404,detail=f"there are no orders with the user_id {find_user_id}")


    


 



        
            