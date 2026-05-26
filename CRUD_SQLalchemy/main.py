from sqlalchemy import Column,create_engine,Integer,String
from sqlalchemy.orm import declarative_base,sessionmaker
from fastapi import FastAPI

angine=create_engine('sqlite:///CRUD_SQLalchemy/data_user.db')
Session=sessionmaker(bind=angine)
session=Session()

app=FastAPI()

base=declarative_base()

class Users(base):
    __tablename__='data_users'
    id=Column(Integer,primary_key=True)
    nama=Column(String)
    kelas=Column(String)
    sekolah=Column(String)

base.metadata.create_all(angine)

@app.post('/data_users')
def tambah(id:int,nama:str,kelas:str,sekolah:str):
    nama=nama.strip().lower()
    kelas=kelas.strip().lower()
    sekolah=sekolah.strip().lower()

    if not nama or not kelas or not sekolah:
        return{'msg':'input tidak lengkap'}
    
    if id<=0:
        return{'msg':'id tidak terdefinisi'}

    hasil=session.query(Users).filter(Users.id==id).first()
    if hasil:
        return{'msg':'Data sudah ada'}
    
    
    data_baru=Users(id=id,nama=nama,kelas=kelas,sekolah=sekolah)
    session.add(data_baru)
    session.commit()
    return{'msg':'Data berhasil ditambah'}
@app.get('/data_users')
def get_data(id:int=None,nama:str=None,kelas:str=None,sekolah:str=None):
    query=session.query(Users)

    if id is not None:
        if id<=0:
            return {'msg':'id tidak valid'}       
        query=query.filter(Users.id==id)

    if nama:
        nama=nama.strip().lower()
        if not nama:
            return{'msg':'input nama kosong'}
        query=query.filter(Users.nama==nama)
    
    if kelas:
        kelas=kelas.strip().lower()
        if not kelas:
            return{'msg':'input kelas kosong'}
        query=query.filter(Users.kelas==kelas)

    if sekolah:
        sekolah=sekolah.strip().lower()
        if not sekolah:
            return{'msg':'input sekolah kosong'}
        query=query.filter(Users.sekolah==sekolah)
    
    hasil=query.all()
    if not hasil:
        return{'msg':'Data tidak ditemukan'}
    
    return[{'id':user.id,
            'nama':user.nama,
            'kelas':user.kelas,
            'sekolah':user.sekolah
            }
            for user in hasil]

@app.put('/data_users/{id}')
def update(id:int,nama:str=None,kelas:str=None,sekolah:str=None):
    if id<=0:
        return{'msg':'id tidak valid'}
    hasil=session.query(Users).filter(Users.id==id).first()
    if not hasil:
        return{'msg':'Data tidak ditemukan'}
    
    if nama:
        nama=nama.strip()
        if not nama:
            return{'msg':'input nama hanya berisi spasi'}
        hasil.nama=nama.lower()
    if kelas:
        kelas=kelas.strip()
        if not kelas:
            return{'msg':'input kelas hanya berisi spasi'}
        hasil.kelas=kelas.lower()
    if sekolah:
        sekolah=sekolah.strip()
        if not sekolah:
            return{'msg':'input sekolah hanya berisi spasi'}
        hasil.sekolah=sekolah.lower()
    
    if not nama and not kelas and not sekolah:
        return{'msg':'tidak ada data yang diupate'}
    
    session.commit()
    return{'msg':'Data berhasil diupdate'}

@app.delete('/data_users/{id}')
def delete(id:int):
    if id<=0:
        return{'msg':'id tidak valid'}
    
    hasil=session.query(Users).filter(Users.id==id).first()
    if not hasil:
        return{'msg':'Data tidak ditemukan'}
    session.delete(hasil)
    session.commit()
    return{'msg':'Data berhasil dihapus'}