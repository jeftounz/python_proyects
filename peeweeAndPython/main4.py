import peewee
#AQUI DEMOSTRAMOS LA RELACION DE MUCHO A MUCHOS EN SQL

database=peewee.MySQLDatabase('pythondb',
                     host='localhost',
                     port=3306,
                     user='root',
                     passwd='admin')

#UN PRODUCTO PUEDE ENCONTRARSE EN MULTIPLES CATEGORIAS Y UNA CATEGORIA PUEDE ESTAR EN MUCHOS PRODUCTOS

class Product(peewee.Model):
    title=peewee.CharField(max_length=50)
    price=peewee.DecimalField(max_digits=10,decimal_places=2)

    class Meta:
        database=database
        db_table='products'

    def __str__(self):
        return self.title

class Category(peewee.Model):
    title=peewee.CharField(max_length=20)

    class Meta:
        database=database
        db_table='categories'

    def __str__(self):
        return self.title

#FUNCION MAIN 4
database.drop_tables([Product,Category])
database.create_tables([Product,Category])

ipad=Product.create(title='Ipad',price=500.50)
iphone=Product.create(title="IPhone",price=800.00)
tv=Product.create(title="Tv",price=600.00)



