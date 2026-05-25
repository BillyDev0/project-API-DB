import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

file='CRUD_with_server/data.csv'
df=pd.read_csv(file)
app=FastAPI()

class komponen(BaseModel):
    id:str
    nama:str
    kelas:str
    sekolah:str

@app.post('/absensi')
def tambah_data(siswa:komponen):
    df=pd.read_csv(file)

    df['id']=df['id'].astype(str)
    siswa.nama=siswa.nama.lower().strip()
    siswa.sekolah=siswa.sekolah.lower().strip()
    siswa.kelas=siswa.kelas.lower().strip()
    
    if not siswa.id or not siswa.nama or not siswa.kelas or not siswa.sekolah:
        return{'msg':'input tidak lengkap'}
    
    if not siswa.id.strip() or not siswa.nama.strip() or not siswa.kelas.strip() or not siswa.sekolah.strip():
        return{'msg':'Data kosong'}
    
    if (df['id']==siswa.id).any() or (df['nama']==siswa.nama).any():
        return{'msg':'Data sudah terdaftar'}
    
    data_baru=pd.DataFrame([{
        'id':siswa.id,
        'nama':siswa.nama,
        'kelas':siswa.kelas,
        'sekolah':siswa.sekolah
    }])

    data_baru.to_csv(file,mode='a',index=False,header=False)
    return{'msg':'Data berhasil ditambah'}


@app.get('/absensi/{id}')
def get_by_id(id:str):
    df=pd.read_csv(file)
    df['id']=df['id'].astype(str)
    
    if not id.strip():
        return{'msg':'Data kosong'}
    
    hasil=df[df['id']==id]
    if not hasil.empty:
        return hasil.to_dict(orient='records')
    else:
        return{'msg':'Data tidak ditemukan'}
    
    
@app.get('/absensi')
def get_all(nama:str=None,kelas:str=None,sekolah:str=None):
    df=pd.read_csv(file)
    
    if nama and nama.strip():
        df=df[df['nama']==nama.lower()]
    if kelas and kelas.strip():
        df=df[df['kelas']==kelas.lower()]
    if sekolah and sekolah.strip():
        df=df[df['sekolah']==sekolah.lower()]

    if df.empty:
        return{'msg':'Data tidak ditemukan'}
    
    
    return df.to_dict(orient='records')


@app.put('/absensi/{id}')
def update_data(id:str=None,nama:str=None,kelas:str=None,sekolah:str=None):
    df=pd.read_csv(file)
    df['id']=df['id'].astype(str)

    hasil=df['id']==id
    if hasil.any():
        if nama and nama.strip():
            df.loc[hasil,'nama']=nama.lower()
        if kelas and kelas.strip():
            df.loc[hasil,'kelas']=kelas.lower()
        if sekolah and sekolah.strip():
            df.loc[hasil,'sekolah']=sekolah.lower()
        
        df.to_csv(file,index=False)
        return{'msg':'Data berhasil diupdate'}
    else:
        return{'msg':'Data tidak ditemukan'}


@app.delete('/absensi/{id}')
def delete_data(id:str=None,nama:str=None,kelas:str=None,sekolah:str=None):
    df=pd.read_csv(file)
    df['id']=df['id'].astype(str)
    
    jumlah_awal=len(df)
    if id and id.strip():
        df=df[df['id']!=id]
    if nama and nama.strip():
        df=df[df['nama']!=nama.lower().strip()]
    if kelas and kelas.strip():
        df=df[df['kelas']!=kelas.lower().strip()]
    if sekolah and sekolah.strip():
        df=df[df['sekolah']!=sekolah.lower().strip()]

    
    if len(df)==jumlah_awal:
        return{'msg':'Data tidak ditemukan'}
    
    df.to_csv(file,index=False)
    return{'msg':'Data berhasil dihapus'}
