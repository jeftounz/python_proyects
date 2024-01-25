
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
try:
    with engine.connect() as connection:
        insert_query=users.insert() #Query -> Insert Into Users

        with open("usuarios.json") as file:
            users=json.load(file)
            connection.execute(insert_query,users)
           # for user in users:
           #    query= insert_query.values(**user)
           #     connection.execute(query)

except Exception as error:
    print(f"Error: {error}")