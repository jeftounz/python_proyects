from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from datetime import datetime
from sqlalchemy.orm import sessionmaker

Base= declarative_base()

engine=create_engine('postgresql://postgre:admin@localhost/pythondb')
class User(Base):
    __tablename__='users'

    id= Column(Integer(),primary_key=True)
    username=Column(String(50),nullbase=False,unique=True)
    email=Column(String(50),nullbase=False,unique=True)
    create_at=Column(datetime(), default=datetime.now())

    def __str__(self):
        return self.username
    
#Necesitamos esta session para poder conectarme a la base de datos (como con peewee y su metadato)    
Session=sessionmaker(engine)
session=Session()

if __name__=='__main__':
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    
