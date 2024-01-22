from sqlalchemy import create_engine #Nos permitira un objeto tipo engine para la conexion
from sqlalchemy import MetaData #Servira de puente entre el programa y el gestor de postgress
from sqlalchemy import Table,Column,Integer,String,DateTime #Seremos capaces de crear objetos de tipo table,columnas enteras y string
from datetime import datetime #Importamos el tiempo
#Vamos a utilziar postgress
engine=create_engine("postgresql://postgres:admin@localhost/project_pythondb")
metadata=MetaData()

#users
users = Table(
    'users',
    metadata,
    Column('id', Integer(), primary_key=True),
    Column('username', String(), index=True, nullable=False),
    Column('email', String(), nullable=False),
    Column('Created_at', DateTime(), default=datetime.now())  # Utilizar DateTime en lugar de datetime()
)


if __name__=='__main__':

    metadata.drop_all(engine)
    metadata.create_all(engine)

    print(users.c.username)