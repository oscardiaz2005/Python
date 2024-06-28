from pydantic  import BaseModel

class order (BaseModel):
    id:str
    id_usuario:str
    lista_productos:list[str]
    total:int