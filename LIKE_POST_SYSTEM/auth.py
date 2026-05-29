from LIKE_POST_SYSTEM.db_setup import session,User,Post,Like
from passlib.hash import bcrypt
from LIKE_POST_SYSTEM.jwt_auth import create_token,verify_token
from fastapi import FastAPI

app=FastAPI()
@app.post('/Login')
def login(username:str,password:str):
    username=username.strip().lower()
    if not username:
        return{'msg':'input username kosong'}
    
    password=password.strip().lower()
    if not password:
        return{'msg':'input password kosong'}
    
    user=session.query(User).filter(User.username==username).first()
    if not user:
        return {'msg':'Data tidak ditemukan'}
    
    if not bcrypt.verify(password,user.password):
        return {'msg':'password salah'}

    
    token=create_token(user.username)
    return {'token':f'{token}'}


@app.post('/Registrasi')
def registrasi(username:str,password:str):
    username=username.strip().lower()
    if not username:
        return{'msg':'input username kosong'}
    
    password=password.strip().lower()
    if not password:
        return{'msg':'input password kosong'}
    
    user=session.query(User).filter(User.username==username).first()
    if user:
        return{'msg':'Data sudah ada'}
    
    hashed_password=bcrypt.hash(password)
    
    new_user=User(username=username,password=hashed_password)
    session.add(new_user)
    session.commit()
    return {'msg':'Registrasi berhasil'}

@app.get('/Post')
def post(token:str):
    cek_token=verify_token(token)
    if not cek_token:
        return{'msg':'token error'}

    user=session.query(Post).all()
    data=[]
    for i in user:
        data.append({"id":i.id,"title":i.title})
    return data

@app.post('/like')
def like(token:str,post_id:str,id:str):
    username=verify_token(token)
    if not username:
        return{'msg':'token error'}
    
    post_id=post_id.strip()
    if not post_id:
        return {'msg':'input id kosong'}
    
    post=session.query(Post).filter(Post.id==post_id).first()
    if not post:
        return{'msg':'konten tidak ditemukan'}
    
    like=session.query(Like).filter(
        Like.username==username,
        Like.post_id==post_id
        ).first()
    
    if like:
        return{'msg':'konten sudah di like'}
    
    new_like=Like(id=id,username=username,post_id=post_id)
    session.add(new_like)
    session.commit()

    return{'msg':'Berhasil di like'}