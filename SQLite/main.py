import sqlite3

db=sqlite3.connect('SQLite/data.db')
cursor=db.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS absensi(
               id TEXT PRIMARY KEY,
               nama TEXT,
               kelas TEXT,
               sekolah TEXT
) ''')
db.commit()

def create():
    cursor.execute('''
    INSERT INTO absensi VALUES ('2', 'Billy','X RPL 2','SMKN 1 DLANGGU')''')
    db.commit()

def update():
    cursor.execute('UPDATE absensi SET nama="Arasya" WHERE id=2 ')
    db.commit()

def read():
    cursor.execute('SELECT * FROM absensi')
    print(cursor.fetchall())

def delete():
    cursor.execute('DELETE FROM absensi WHERE id=2')
    db.commit()

delete()
read()