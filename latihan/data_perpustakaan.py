from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

data_siswa=[]
class Siswa(BaseModel):
    nama:str
    kelas:str
    judul_buku:str

@app.post('/perpustakaan')
def pinjam_buku(siswa:Siswa):
    data_siswa.append(siswa)
    return{'Data berhasil ditambah'}

@app.get('/perpustakaan')
def get_data_siswa():
    return data_siswa

@app.get('/perpustakaan/{nama}')
def get_byNama(nama:str):
    for siswa in data_siswa:
        if siswa.nama == nama:
            return siswa
            
    return{'error':'Data tidak ditemukan'}