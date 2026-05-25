from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

data_siswa = [
    {'id': '1', 'nama': 'Billy', 'kelas': '10 RPL 3', 'sekolah': 'SMPN 1 PURI'},
    {'id': '2', 'nama': 'Andi', 'kelas': '10 RPL 1', 'sekolah': 'SMPN 2 PURI'},
    {'id': '3', 'nama': 'Sinta', 'kelas': '10 RPL 2', 'sekolah': 'SMPN 3 PURI'},
    {'id': '4', 'nama': 'Raka', 'kelas': '10 RPL 3', 'sekolah': 'SMPN 1 PURI'},
    {'id': '5', 'nama': 'Dewi', 'kelas': '10 RPL 1', 'sekolah': 'SMPN 2 PURI'}
]

@app.delete('/absensi/{id}')
def delete_siswa(id:str):
    for item in data_siswa:
        if id == item['id']:
            data_siswa.remove(item)

            return{'msg':'Data berhasil dihapus'}
    
    return{'msg':'Data tidak ditemukan'}