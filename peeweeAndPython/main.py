import peewee #Podemos interactuar con la base de datos mediante objetos .Utilizaremos mySQL 
from datetime import datetime #Esta libreria de windows nos dara la instancia

database=peewee.MySQLDatabase('pythondb',
                     host='localhost',
                     port=3306,
                     user='root',
                     passwd='admin')

# tabla users
class User(peewee.Model):
    username= peewee.CharField(max_length=50,unique=True,index=True) 
    email=peewee.CharField(max_length=60,null=False) 
    active=peewee.BooleanField(default=False)
    created_at=peewee.DateTimeField(default=datetime.now)

    class Meta:
        database=database
        db_table='users'


if __name__=='__main__':
        
    if User.table_exists(): #Creamos nuesta tabla como una clase
        User.drop_table()
    
    User.create_table()
