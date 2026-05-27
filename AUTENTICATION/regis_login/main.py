from passlib.hash import bcrypt
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from fastapi import FastAPI

angine=create_engine('sqlite:///AUTENTICATION/regis_login/data.db')
Session=sessionmaker(bind=angine)
session=Session()
base=declarative_base()

app=FastAPI

class User(base):
    __tablename__='users'

    username=Column(String,primary_key=True)
    password=Column(String)

base.metadata.create_all(angine)


def Register(username:str,password:str):
    username=username.strip().lower()
    if not username:
        return{'msg':'input username kosong'}
    
    user=session.query(User).filter(User.username==username).first()
    if user:
        return{'msg':'Data sudah ada'}
    
    password=password.strip()
    if not password:
        return {'msg':'input password kosong'}
    hashed_password=bcrypt.hash(password)

    user_baru=User(username=username,password=hashed_password)
    session.add(user_baru)
    session.commit()

    return {'msg':'Registrasi berhasil'}

def Login(username:str,password:str):
    username=username.strip().lower()
    if not username:
        return{'msg':'input username kosong'}
    
    user=session.query(User).filter(User.username==username).first()
    if not user:
        return{'msg':'Data tidak ditemukan'}
    
    password=password.strip()
    if not bcrypt.verify(password,user.password):
        return{'msg':'password salah'}
    
    return{'msg':'Login berhasil'}


print(Register("a", "   "))
print(Login("rizky", "123456"))
print(Login("rizky", "salah"))