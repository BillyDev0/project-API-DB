from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
data_order=[]

class Order(BaseModel):
    user_name:str
    item:str
    jumlah:int

@app.post('/order')
def order(order:Order):
    data_order.append(order)
    return {'msg':'Order berhasil ditambahkan'}

@app.get('/order')
def get_order():
    return data_order

@app.get('/order/{id}')
def get_order_byid(id:int):
    if id>=len(data_order):
        return {'error':'Data tidak ditemukan'}
    return data_order[id]

