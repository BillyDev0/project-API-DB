from .jwt_auth import create_token
from .db_setup import session,User
from passlib.hash import bcrypt


def login(username:str,password:str):
    username=username.strip()
    if not username:
        return{'msg':'input username kosong'}
    
    password=password.strip()
    if not password:
        return{'msg':'input password  kosong'}
    
    user=session.query(User).filter(User.username==username).first()
    if not user:
        return{'msg':'Akun tidak ditemukan'}
    
    if not bcrypt.verify(password,user.password):
        return{'msg':'password salah'}
    
    token=create_token(user.username)

    return {'token':token}

def registrasi(username:str,password:str):
    username=username.strip()
    if not username:
        return{'msg':'input username kosong'}
    
    password=password.strip()
    if not password:
        return{'msg':'input password  kosong'}
    
    user=session.query(User).filter(User.username==username).first()
    if user:
        return{'msg':'Akun sudah ada'}
    
    hashed_password=bcrypt.hash(password)

    new_user=User(username=username,password=hashed_password)
    session.add(new_user)
    session.commit()

    return{'msg':'Registrasi berhasil'}

