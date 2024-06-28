from fastapi import FastAPI, HTTPException
from ModelProduct import Product
import json

app = FastAPI()

with open("Catalogue.json", "r") as txt:
    data_product = json.load(txt)
    product_list = [Product(**i) for i in data_product]


#2. Ruta POST para crear un nuevo Producto
@app.post("/addProduct", response_model=Product)
async def add_new_product(new_product: Product):
    if new_product.stock<=0 or new_product.price<=0:
        raise HTTPException(status_code=404, detail="The price and the stock must be greater than 0.")   
     
    for product in product_list:
        if product.id == new_product.id :
            raise HTTPException(status_code=404, detail="The product is already in the catalogue")
    product_list.append(new_product)
      
    with open("Catalogue.json", "w") as txt:
        json.dump([i.dict() for i in product_list], txt, indent=4)  
    
    raise HTTPException(status_code=200, detail=f"the product {new_product.name} was added")
    


#3. Ruta GET para obtener todos los Productos:
@app.get("/allProducts")
async def show_all_products ():
    if product_list:
        return product_list 

    raise HTTPException(status_code=404 , detail="The catalogue is empty.")
    

#4. Ruta GET para obtener un Producto por su id:
@app.get("/productById/{id}")
async def find_product_id(id:str):
    for product in product_list:
        if product.id == id:
            return product
    raise HTTPException(status_code=404,detail="the product does not exist")


#5. Ruta PUT para actualizar un Producto existente
@app.put("/updateProduct/{find_id}",response_model=Product)
async def update_product(find_id:str,update_product:Product):
    if update_product.price<=0 or update_product.stock<=0:
        raise HTTPException(status_code=404, detail="The price and the stock must be greater than 0.")    
    
    
    for i,product in enumerate(product_list):
        if product.id==find_id:
            product_list[i]=update_product
            with open("Catalogue.json" , "w") as txt:
                json.dump([i.dict() for i in product_list],txt,indent=4)
                raise HTTPException(status_code=200,detail=f"the product with the id {product.id} was updated")
        raise HTTPException (status_code=404,detail=f"the id {find_id} does not exist")        
        

#6. Ruta DELETE para eliminar un Producto:
@app.delete("/deleteProduct/{find_id}")        
async def deleteProduct(find_id: str):
    for product in product_list:
        if product.id==find_id:
            product_list.remove(product)
            with open ("Catalogue.json", "w") as txt :
                json.dump([i.dict() for i in product_list],txt, indent=4)
                return f"the product with the id {find_id} was deleted"
 
    raise HTTPException (status_code=404,detail=f"the id {find_id} does not exist")        
