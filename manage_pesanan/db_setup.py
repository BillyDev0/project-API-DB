from sqlalchemy import Column,String,Integer,create_engine
from sqlalchemy.orm import declarative_base,sessionmaker

engine=create_engine('sqlite:///manage_pesanan/data.db')
Session=sessionmaker(bind=engine)
session=Session()
base=declarative_base()

class Pesanan(base):
    __tablename__='data_pesanan'

    id_pesanan=Column(Integer,primary_key=True,autoincrement=True)
    nama_pembeli=Column(String)
    pesanan=Column(String)
    status=Column(String,default='belum')

class User(base):
    __tablename__='data_user'

    username=Column(String,primary_key=True)
    password=Column(String)

base.metadata.create_all(engine)
