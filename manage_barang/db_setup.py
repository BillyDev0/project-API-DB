from sqlalchemy import Column,String,Integer,create_engine
from sqlalchemy.orm import declarative_base,sessionmaker

engine=create_engine("sqlite:///manage_barang/db_barang.db")
Sesion=sessionmaker(bind=engine)
session=Sesion()
base=declarative_base()

class Barang(base):
    __tablename__='data_barang'

    nama_barang=Column(String,primary_key=True)
    harga_barang=Column(Integer)
    stok_barang=Column(Integer)

class User(base):
    __tablename__='data_user'

    username=Column(String,primary_key=True)
    password=Column(String)

class Transaksi(base):
    __tablename__='data_transaksi'
    
    id=Column(Integer,primary_key=True,autoincrement=True)
    username=Column(String)
    nama_barang=Column(String)
    jumlah_beli=Column(Integer)

base.metadata.create_all(engine)

