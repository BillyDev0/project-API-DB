from manage_barang.jwt_auth import verify_token,create_token
from manage_barang.db_setup import Barang,User,Transaksi,session
from fastapi import FastAPI
from passlib.hash import bcrypt

app=FastAPI()

@app.post('/registrasi')
def Registrasi(username:str,password:str):
    username=username.strip().lower()
    if not username:
        return {'msg':'input username kosong'}
    
    password=password.strip()
    if not password:
        return{'msg':'input password kosong'}
    
    user=session.query(User).filter(User.username==username).first()
    if user:
        return{'msg':'akun sudah terdaftar'}
    
    hashed_password=bcrypt.hash(password)
    new_user=User(username=username,password=hashed_password)
    
    session.add(new_user)
    session.commit()
    return{'msg':'Registrasi berhasil'}


@app.post('/login')
def Login(username:str,password:str):
    username=username.strip().lower()
    if not username:
        return {'msg':'input username kosong'}
    
    password=password.strip()
    if not password:
        return{'msg':'input password kosong'}
    
    user=session.query(User).filter(User.username==username).first()
    if not user:
        return{'msg':'Akun tidak ditemukan'}
    
    if not bcrypt.verify(password,user.password):
        return{'msg':'password salah'}
    
    token=create_token(username)
    return {'token':token}
    
@app.put('/data_pembelian')
def pembelian_barang(token:str,nama_barang:str,jumlah_beli:int):
    cek_token=verify_token(token)
    if not cek_token:
        return {'msg':'token error'}
    
    nama_barang=nama_barang.strip().lower()
    if not nama_barang:
        return {'msg':'input nama barang kosong'}

    barang=session.query(Barang).filter(Barang.nama_barang==nama_barang).first()
    if not barang:
        return{'msg':'Barang tidak ditemukan'}
    
    if jumlah_beli<=0:
        return {'msg':'jumlah tidak valid'}
    
    cek_stok=barang.stok_barang-jumlah_beli
    if cek_stok<0:
        return {'msg':'Stok barang tidak cukup'}
    
    barang.stok_barang=barang.stok_barang-jumlah_beli
    new_transaksi=Transaksi(username=cek_token,nama_barang=nama_barang,jumlah_beli=jumlah_beli)

    session.add(new_transaksi)
    session.commit()
    return {'msg':'pembelian berhasil'}


@app.get('/data_barang')
def get_data_barang(token:str):
    cek_token=verify_token(token)
    if not cek_token:
        return{'msg':'Token error'}
    
    barang=session.query(Barang).all()
    data=[]
    for i in barang:
        data.append({
            'nama_barang':i.nama_barang,
            'harga_barang':i.harga_barang,
            'stok_barang':i.stok_barang
        })
    return data

@app.put('/data_barang')
def tambah_stok(token:str,nama_barang:str,stok_tambahan:int):
    cek_token=verify_token(token)
    if not cek_token:
        return{'msg':'Token error'}

    nama_barang=nama_barang.strip().lower()
    if not nama_barang:
        return {'msg':'input nama barang kosong'}
    
    if stok_tambahan<=0:
        return {'msg':'input stok tidak valid'}
    
    barang=session.query(Barang).filter(Barang.nama_barang==nama_barang).first()
    if not barang:
        return{'msg':'Barang tidak ditemukan'}
    
    barang.stok_barang=barang.stok_barang+stok_tambahan
    session.commit()
    return{'msg':'stok berhasil diupdate'}


@app.post('/data_barang')
def tambah_barang(token:str,nama_barang:str,harga_barang:int,stok_barang:int):
    cek_token=verify_token(token)
    if not cek_token:
        return{'msg':'token error'}
    
    nama_barang=nama_barang.strip().lower()
    if not nama_barang:
        return {'msg':'input nama barang kosong'}
    if harga_barang<=0:
        return{'msg':'input harga barang tidak valid'}
    if stok_barang<=0:
        return {'msg':'input stok barang tidak valid'}
    
    barang=session.query(Barang).filter(Barang.nama_barang==nama_barang).first()
    if barang:
        return {'msg':'Barang sudah tersedia'}
    
    new_barang=Barang(nama_barang=nama_barang,harga_barang=harga_barang,stok_barang=stok_barang)
    session.add(new_barang)
    session.commit()
    return{'msg':'Barang berhasil ditambahkan'}



