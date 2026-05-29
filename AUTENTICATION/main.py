from AUTENTICATION.auth import Registrasi,Login
from fastapi import FastAPI
from AUTENTICATION.jwt_auth import verify_token

app=FastAPI()

@app.post('/registrasi')
def regist(username:str,password:str):
    return Registrasi(username,password)

@app.post('/login')
def login(username:str,password:str):
    return Login(username,password)

@app.get('/data_user')
def get_user(token):
    user=verify_token(token)
    if not user:
        return{'msg':'Token bermasalah'}
    
    return {'msg':f'Halo {user}'}
