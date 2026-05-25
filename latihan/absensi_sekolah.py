from pydantic import BaseModel
from fastapi import FastAPI

app=FastAPI()
data_absensi=[]

class komponen(BaseModel):
    nama:str
    kelas:str
    status_hadir:str
    waktu:int

@app.post('/absensi')
def post_absensi(siswa:komponen):
    siswa.nama=siswa.nama.lower()
    siswa.kelas=siswa.kelas.strip().lower()
    siswa.status_hadir=siswa.status_hadir.lower()

    if siswa.status_hadir!='hadir' and siswa.status_hadir!='izin' and siswa.status_hadir!='alpha':
        return{'msg':'Data Absensi tidak sesuai ketentuan'}

    data_absensi.append(siswa)
    return {'msg':'Absen berhasil ditambah'}

@app.get('/absensi')
def get_(kelas:str=None,status_hadir:str=None,sort:str=None,):
    data_filter=data_absensi

    if kelas:
        data_filter=[item for item in data_filter if item.kelas == kelas.lower()]
    if status_hadir:
        data_filter=[item for item in data_filter if item.status_hadir == status_hadir.lower()]
    if sort:
        if sort=='waktu':
            data_filter=sorted(data_filter,key=lambda x:x.waktu,reverse=False)

        else:
            return {'msg':'Data tidak ditemukan'}
    

    if not data_filter:
        return{'msg':'Data tidak ada'}
    
    return data_filter

@app.get('/absensi/total')
def get_total():
    total=len(data_absensi)
    return {'Total siswa':total}

@app.get('/absensi/rekap')
def get_rekap():
    data_hadir=[item for item in data_absensi if item.status_hadir=='hadir']
    data_izin=[item for item in data_absensi if item.status_hadir=='izin']
    data_alpha=[item for item in data_absensi if item.status_hadir=='alpha']

    return {
        'hadir':len(data_hadir),
        'izin':len(data_izin),
        'alpha':len(data_alpha)
    }

    