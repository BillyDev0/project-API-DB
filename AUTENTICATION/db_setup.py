from sqlalchemy import String,Column,create_engine
from sqlalchemy.orm import declarative_base,sessionmaker

engine=create_engine('sqlite:///AUTENTICATION/db.db')
Sesion=sessionmaker(bind=engine)
session=Sesion()

base=declarative_base()

class User(base):
    __tablename__='users'

    username=Column(String,primary_key=True)
    password=Column(String)

base.metadata.create_all(engine)
