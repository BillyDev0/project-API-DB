from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()
data_produk=[]


class komponen_produk(BaseModel):
    nama:str
    harga:int
    kategori:str


@app.post('/data_produk')
def post_produk(produk:komponen_produk):
    if produk.harga<=0:
        return{'msg':'Harga harus lebih dari Rp0'}
    
    data_produk.append(produk)
    return {'msg':'Data berhasil ditambah'}

@app.get('/data_produk')
def get_all():
    return data_produk


@app.get('/data_produk')
def get_by_nama(nama_produk:str):
    for item in data_produk:
        if item.nama == nama_produk:
            return item

    return {'msg':'Data tidak ada'}
        
    
