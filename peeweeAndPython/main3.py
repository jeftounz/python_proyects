import peewee
#AQUI DEMOSTRAMOS LA RELACION DE UNO A UNO EN SQL
database=peewee.MySQLDatabase('pythondb',
                     host='localhost',
                     port=3306,
                     user='root',
                     passwd='admin')

class User(peewee.Model):
    username=peewee.CharField(max_length=50)
    email=peewee.CharField(max_length=50)
    class Meta:
        database=database
        db_table='users'

    def __str__(self):
        return self.username  

    @property    #Este decorador hace que los metodos se ejecuten como atributos
    def admin(self):
        return self.admins.first()  

class Admin(peewee.Model):
    permission_level=peewee.IntegerField(default=1)
    user=peewee.ForeignKeyField(User,backref='admins',unique=True) #Aqui va la relacion con la tabla user

    class Meta:
        database=database
        db_table="admins"

    def __str__(self):
        return f'admin{self.id}'




#FUNCION MAIN
    
database.drop_tables([User,Admin])    
database.create_tables([User,Admin])

user1=User.create(username="User1",email="user1@gmail.com")
admin1=Admin.create(permission_level=10,user=user1)

#print(admin1.user.username)
#print(admin1.user.email)

print(user1.admin)