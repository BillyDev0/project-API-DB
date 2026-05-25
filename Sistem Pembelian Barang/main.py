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

@app.get('/data_barang')
def beli_barang(nama_barang:str,jumlah_beli:int):
    
    nama_barang=nama_barang.strip().lower()

    if not nama_barang:
        return{'msg':'input nama_barang hanya berisi spasi'}

    cek_nama_barang=session.query(Barang).filter(Barang.nama_barang==nama_barang).first()

    if not cek_nama_barang:
        return{'msg':'Data tidak ditemukan'}

    if jumlah_beli<=0:
       return{'msg':'Data tidak valid'}
    
    if jumlah_beli>cek_nama_barang.stok_barang:
        return{'msg':'stok barang tidak cukup'}

    
    cek_nama_barang.stok_barang-=jumlah_beli
    total_bayar=jumlah_beli * cek_nama_barang.harga_barang
    
    session.commit()
    return{'nama_barang':cek_nama_barang.nama_barang,
           'jumlah_beli':jumlah_beli,
           'total_bayar':total_bayar,
           'sisa_stok':cek_nama_barang.stok_barang
            }