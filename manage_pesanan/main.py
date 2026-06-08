from .db_setup import session,User,Pesanan
from .jwt_auth import verifikasi_token
from .auth import login,registrasi
from fastapi import FastAPI

app=FastAPI()

@app.post('/login')
def Login(username:str,password:str):
    return login(username,password)

@app.post('/Registrasi')
def Registrasi(username:str,password:str):
    return registrasi(username,password)

@app.post('/pesanan')
def tambah_pesanan(token:str,pesanan:str):
    username=verifikasi_token(token)
    if not username:
        return{'msg':'token error'}

    pesanan=pesanan.strip()
    if not pesanan:
        return{'msg':'input pesanan kosong'}
    
    new_pesanan=Pesanan(nama_pembeli=username,pesanan=pesanan)
    session.add(new_pesanan)
    session.commit()
    return{'msg':'pesanan berhasil ditambah'}

@app.get('/pesanan')
def data_pesanan(token:str):
    cek_token=verifikasi_token(token)
    if not cek_token:
        return{'msg':'token error'}
    data=session.query(Pesanan).all()
    data_list_pesanan=[]
    for i in data:
        data_list_pesanan.append({
            'id_pesanan':i.id_pesanan,
            'nama_pembeli':i.nama_pembeli,
            'pesanan':i.pesanan,
            'status':i.status
        })
    return data_list_pesanan

@app.put('/pesanan/selesai')
def selesai(token:str,id:int):
    user=verifikasi_token(token)
    if not user:
        return{'msg':'token error'}
    
    if id<=0:
        return{'msg':'id tidak valid'}
    pesanan=session.query(Pesanan).filter(Pesanan.id_pesanan==id).first()
    if not pesanan:
        return{'msg':'pesanan tidak ditemukan'}
    
    pesanan.status='sudah'
    session.commit()
    return{'msg':f'pesanan id {id} sudah selesai'}
    