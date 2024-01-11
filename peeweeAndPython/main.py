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
    
    def __str__(self):
        return self.username


if __name__=='__main__':
        
    if User.table_exists(): #Creamos nuesta tabla como una clase
        User.drop_table()
    
    User.create_table()

    #METODOS PARA INSERTAR REGISTROS
    """#METODO 1:
    user1=User(username='user1',email='user1@ejemplo.com',active=True)
    user1.save()

    #METODO 2:
    user2= User()
    user2.username='user2'
    user2.email='user2@gmail.com'
    user2.save()

    #METODO 3:

    values={
        'username': 'user3',
        'email': 'user3@gmail.com'
    }

    user3=User(**values)
    user3.save()

    #METODO 4:
    user4=User.create(username='user4',email='user4@gmail.com')
    print(user4.id)

    #METODO 5
    query=User.insert(username="user5",email="user5@gmail.com")
    print(type(query)) #Se devuelve un query con el metodo insert para su ejecucion
    query.execute()"""

    #METODO PARA MULTIPLES REGISTROS
    users=[{"username":"user1","email":"user1@gmail.com",'active':True},
           {"username":"user2","email":"user2@gmail.com"},
           {"username":"user3","email":"user3@gmail.com",'active':True},
           {"username":"user4","email":"user4@gmail.com",},
           {"username":"user5","email":"user5@gmail.com"},
           {"username":"user6","email":"user6@gmail.com",'active':True},
           {"username":"user7","email":"user7@gmail.com",'active':True},]
    
    query=User.insert_many(users)
    query.execute()

    #OBTENER REGISTROS OH CONSULTAS
    #SELECT username, email from users; es lo que significa y el .where es para discriminar
    users=User.select(User.username,
                      User.email,
                      User.active
        ).where(
        (User.active==True) & 
        (
            (User.id==1) | (User.id==7)
        )
        
        )

    #Imprimimos los registros
    for user in users:
        print(user)
