import json
from datetime import datetime #Importamos el tiempo
from sqlalchemy import create_engine #Nos permitira un objeto tipo engine para la conexion
from sqlalchemy import MetaData #Servira de puente entre el programa y el gestor de postgress
from sqlalchemy import Table,Column,Integer,String,DateTime #Seremos capaces de crear objetos de tipo table,columnas enteras y string


engine=create_engine("postgresql://postgres:admin@localhost/project_pythondb")
metadata=MetaData()

#users
users=Table(
    'users',
    metadata,
    Column('id',Integer(),primary_key=True),
    Column('age',Integer),
    Column('country',String(56),nullable=False),
    Column('email',String(50),nullable=False),
    Column('gender',String(6),nullable=False),
    Column('name',String(50),nullable=False)
)

#FUNCION MAIN2


metadata.drop_all(engine)
metadata.create_all(engine)

with engine.connect() as connection:
    with open('usuarios.json') as file:
        connection.execute(users.insert(),json.load(file))
    select_query=users.select()

    result=connection.execute(select_query) #ResultProxy

    for user in result.fetchall():
        print(user) #RowProxy