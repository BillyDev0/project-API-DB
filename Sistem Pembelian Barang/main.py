from sqlalchemy import Column,String,Integer,create_engine
from sqlalchemy.orm import declarative_base,sessionmaker
from fastapi import FastAPI

app=FastAPI()

engine=create_engine('sqlite:///Sistem Pembelian Barang/data_barang.db')
Session=sessionmaker(bind=engine)
session=Session()

base=declarative_base()

class Barang(base):
    __tablename__='data_barang'
    nama_barang=Column(String,primary_key=True)
    harga_barang=Column(Integer)
    stok_barang=Column(Integer)

base.metadata.create_all(engine)