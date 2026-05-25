from sqlalchemy import Column,String,Integer,create_engine
from sqlalchemy.orm import declarative_base,sessionmaker
from fastapi import FastAPI

app=FastAPI()
angine=create_engine('sqlite:///SQLAlchemy/update_barang/data.db')
Session=sessionmaker(bind=angine)
session=Session()

base=declarative_base()

class Barang(base):
    __tablename__='data_barang'
    nama_barang=Column(String,primary_key=True)
    harga_barang=Column(Integer)
    stok_barang=Column(Integer)

base.metadata.create_all(angine)


@app.get('/data_barang')
def get_barang():
    hasil=session.query(Barang).all()
    if not hasil:
        return {'msg':'Data belum ada'}
    
    data=[]
    for i in hasil:
        data.append({"nama_barang":i.nama_barang,
               "harga_barang":i.harga_barang,
               "stok_barang":i.stok_barang
               })
    return data

@app.post('/data_barang')
def tambah_barang(nama_barang:str,harga_barang:int,stok_barang:int):
    data=Barang(nama_barang=nama_barang,harga_barang=harga_barang,stok_barang=stok_barang)
    session.add(data)
    session.commit()
    return{'msg':'Data berhasil ditambah'}


@app.put('/data_barang')
def update_data(nama_barang:str,harga_barang:int=None,stok_barang:int=None):
    hasil=session.query(Barang).filter(Barang.nama_barang==nama_barang).first()
    if not hasil:
        return{'msg':'Data tidak ditemukan'}
    
    hasil.harga_barang=harga_barang
    hasil.stok_barang=stok_barang
    session.commit()
    return{'msg':'Data berhasil diupdate'}

@app.delete('/data_barang')
def delete_data(nama_barang:str):
    hasil=session.query(Barang).filter(Barang.nama_barang==nama_barang).first()
    if not hasil:
        return{'msg':'Data tidak ditemukan'}
    
    session.delete(hasil)
    return{'msg':'Data berhasil dihapus'}