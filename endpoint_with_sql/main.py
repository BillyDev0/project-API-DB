import sqlite3
from fastapi import FastAPI

file='endpoint_with_sql/data_barang.db'


app=FastAPI()

db=sqlite3.connect(file)
cursor=db.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS data_barang(
            nama_barang TEXT PRIMARY KEY,
            harga_barang INT,
            jumlah_barang INT
            )''')
db.cursor()

@app.post('/data_barang')
def tambah_barang(nama_barang:str,harga_barang:int,jumlah_barang:int):
    db=sqlite3.connect(file)
    cursor=db.cursor()
    
    nama_barang=nama_barang.strip().lower()
    if not nama_barang:
        return{'msg':'Input tidak lengkap'}
    if harga_barang<=0:
        return{'msg':'Harga tidak wajar'}
    if jumlah_barang<=0:
        return{'msg':'Jumlah tidak valid'}
    
    
    cursor.execute('SELECT * FROM data_barang WHERE nama_barang = ?',
                   (nama_barang,))
    
    hasil_cursor=cursor.fetchall()
    if hasil_cursor:
        return{'msg':'Data sudah ada'}
    
    cursor.execute('INSERT INTO data_barang VALUES(?,?,?)',
                   (nama_barang,harga_barang,jumlah_barang))
    
    db.commit()
    return{'msg':'Data berhasil ditambah'}


@app.get('/data_barang')
def get(nama_barang:str=None,max_harga:int=None,min_harga:int=None):
    db=sqlite3.connect(file)
    cursor=db.cursor()

    if nama_barang :
        nama_barang=nama_barang.strip().lower()
        cursor.execute('SELECT *FROM data_barang WHERE nama_barang = ?',
                       (nama_barang,))
    
        hasil_cursor=cursor.fetchone()
        if not hasil_cursor:
           return {'msg':'Data tidak ditemukan'}
        
        return hasil_cursor
    
    if max_harga or min_harga:
        if  max_harga is not None and min_harga is not None:
            cursor.execute('SELECT * FROM data_barang WHERE harga_barang <= ? and harga_barang >= ?',
                           (max_harga,min_harga))
        if max_harga is not None:
            cursor.execute('SELECT * FROM data_barang WHERE harga_barang<=?',
                           (max_harga,))
        if min_harga is not None:
            cursor.execute('SELECT * FROM data_barang WHERE harga_barang>=?',
                           (min_harga,))
        

        hasil_cursor=cursor.fetchall()
        if not hasil_cursor:
            return{'msg':'Data tidak ditemukan'} 
        return hasil_cursor
    
    cursor.execute('SELECT * FROM data_barang')
    hasil_cursor=cursor.fetchall()
    return hasil_cursor

@app.put('/data_barang')
def update_data(nama_barang:str,harga_barang:int=None,jumlah_barang:int=None):
    db=sqlite3.connect(file)
    cursor=db.cursor()

    if nama_barang:
        nama_barang=nama_barang.strip().lower()
        cursor.execute('SELECT * FROM data_barang WHERE nama_barang = ?',
                       (nama_barang,))
        hasil_cursor=cursor.fetchone()
        if not hasil_cursor:
            return{'msg':'Data tidak ditemukan'}
        
        if harga_barang is not None:
            if harga_barang<=0:
                return{'msg':'Harga barang tidak wajar'}
            cursor.execute('UPDATE data_barang SET harga_barang=? WHERE nama_barang=?',
                           (harga_barang,nama_barang))
            
        if jumlah_barang is not None:
            if jumlah_barang<=0:
                return{'msg':'Jumlah barang tidak valid'}
            cursor.execute('UPDATE data_barang SET jumlah_barang=? WHERE nama_barang=?',
                           (jumlah_barang,nama_barang))
            
        if harga_barang is None and jumlah_barang is None:
            return{'msg':'Tidak ada data yang diupdate'} 
        
        db.commit()
        return{'msg':'Data berhasil diupdate'}
    
    
@app.delete('/absensi')
def detete_data(nama_barang:str):
    db=sqlite3.connect(file)
    cursor=db.cursor()

    if nama_barang:
        nama_barang=nama_barang.strip().lower()

        cursor.execute('SELECT * FROM data_barang WHERE nama_barang=?',
                       (nama_barang,))
        hasil_cursor=cursor.fetchall()
        if not hasil_cursor:
            return{'msg':'Data tidak ditemukan'}
        
        cursor.execute('DELETE FROM data_barang WHERE nama_barang=?',
                       (nama_barang,))
        db.commit()
        return{'msg':'Data berhasil dihapus'}
    
    else:
        return{'msg':'input nama kosong'}
        