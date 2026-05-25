import sqlite3
from fastapi import FastAPI

app=FastAPI()
file='latihan/inventory_mini/data_inventory.db'

db=sqlite3.connect(file)
cursor=db.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS data_inventory(
               nama_barang TEXT PRIMARY KEY,
               stok_barang INT
               )''')
db.commit()

@app.post('/data_inventory')
def tambah_data(nama_barang:str,stok_barang:int):
    db=sqlite3.connect(file)
    cursor=db.cursor()
    
    nama_barang=nama_barang.strip().lower()
    cursor.execute('SELECT * FROM data_inventory WHERE nama_barang = ?',
                   (nama_barang,))
    hasil_cursor=cursor.fetchone()

    if not nama_barang:
        return{'msg':'nama_barang kosong'}
    if hasil_cursor:
        return{'msg':'Data sudah ada'}
    if stok_barang<=0:
        return{'msg':'Jumlah stok tidak valid'}
    
    cursor.execute('INSERT INTO data_inventory VALUES(?,?)',
                   (nama_barang,stok_barang))
    db.commit()
    return{'msg':'Data berhasil ditambah'}

@app.get('/data_inventory')
def get_all():
    db=sqlite3.connect(file)
    cursor=db.cursor()

    cursor.execute('SELECT * FROM data_inventory')
    hasil_cursor=cursor.fetchall()
    return hasil_cursor

@app.put('/data_inventory')
def update_stok(nama_barang:str,tambah_stok:int=None,kurang_stok:int=None):
    db=sqlite3.connect(file)
    cursor=db.cursor()

    nama_barang=nama_barang.strip().lower()
    if not nama_barang:
        return{'msg':'input nama_barang kosong'}
    

    cursor.execute('SELECT * FROM data_inventory WHERE nama_barang = ?',
                   (nama_barang,))
    
    hasil_cursor=cursor.fetchone()
    if not hasil_cursor:
        return{'msg':'Data tidak ditemukan'}
    
            
    stok_lama=hasil_cursor[2]

    if tambah_stok is not None and kurang_stok is not None or tambah_stok is None and kurang_stok is None:
            return{'msg':'Pilihan tidak bisa dilakukan'}
        
    elif tambah_stok is not None:
        if stok_lama + tambah_stok < 0:
                return{'msg':'Stok tidak cukup'}
            
        cursor.execute(f'UPDATE data_inventory SET stok_barang = stok_barang + ? WHERE nama_barang = ? ',
                            (tambah_stok,nama_barang))
        
    elif kurang_stok is not None:
            if kurang_stok <=0:
                return{'msg':'jumlah stok tidak valid'}
            if stok_lama - kurang_stok <0 :
                return {'msg':'Stok tidak cukup'}
            
            cursor.execute(f'UPDATE data_inventory SET stok_barang=stok_barang - ? WHERE nama_barang= ? ',
                            (kurang_stok,nama_barang))
        
    db.commit()
    return{'msg':'Data berhasil diupdate'}
        
        
    

    
    