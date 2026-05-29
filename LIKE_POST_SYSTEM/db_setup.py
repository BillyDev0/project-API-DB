from sqlalchemy import Column,String,create_engine
from sqlalchemy.orm import declarative_base,sessionmaker

engine=create_engine('sqlite:///LIKE_POST_SYSTEM/db_user.db')
Session=sessionmaker(bind=engine)
session=Session()
Base=declarative_base()

class User(Base):
    __tablename__='data_User'

    username=Column(String,primary_key=True)
    password=Column(String)

class Post(Base):
    __tablename__='data_post'

    id=Column(String,primary_key=True)
    title=Column(String)

class Like(Base):
    __tablename__='data_like'

    id=Column(String,primary_key=True)
    username=Column(String)
    post_id=Column(String)

    
Base.metadata.create_all(engine)

