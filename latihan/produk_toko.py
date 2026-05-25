from fastapi import FastAPI
from pydantic import BaseModel
    
app = FastAPI()
data_produk=[]

class komponen_produk(BaseModel):
    nama:str
    harga:int
    kategori:str

@app.post('/produk_toko')
def post_produk(produk:komponen_produk):
    if produk.harga<=0:
        return{'msg':'Harga harus lebih dari Rp0.'}
    
    data_produk.append(produk)
    return{'msg':'Data berhasil ditambah'}


@app.get('/produk_toko')
def get_produk(nama:str=None,max_harga:int=None,kategori:str=None,sort:str=None,top_harga:str=None):
    data_filter=data_produk
    if nama:
        data_filter=[item for item in data_filter if item.nama == nama]

    if kategori:
        data_filter=[item for item in data_filter if item.kategori == kategori]

    if max_harga:
        data_filter=[item for item in data_filter if item.harga <= max_harga ]
    
    if sort.lower()=='harga':
        data_filter=sorted(data_filter, key=lambda x:x.harga,reverse=True)


    if not data_filter:
        return{'msg':'Data tidak ada'}
    
    return data_filter
    

        
    

