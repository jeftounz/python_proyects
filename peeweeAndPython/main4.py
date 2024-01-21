import peewee

# AQUÍ DEMOSTRAMOS LA RELACION DE MUCHO A MUCHOS EN SQL

database = peewee.MySQLDatabase('pythondb',
                                host='localhost',
                                port=3306,
                                user='root',
                                passwd='admin')

# UN PRODUCTO PUEDE ENCONTRARSE EN MÚLTIPLES CATEGORÍAS Y UNA CATEGORÍA PUEDE ESTAR EN MUCHOS PRODUCTOS

class Product(peewee.Model):
    title = peewee.CharField(max_length=50)
    price = peewee.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        database = database
        db_table = 'products'

    def __str__(self):
        return self.title

class Category(peewee.Model):
    title = peewee.CharField(max_length=20)

    class Meta:
        database = database
        db_table = 'categories'

    def __str__(self):
        return self.title

class ProductCategory(peewee.Model):
    product = peewee.ForeignKeyField(Product,backref='categories') #Como es muchos a muchos es a la inversa backref de products: categories
    category = peewee.ForeignKeyField(Category,backref='products') #Backref de categories: products
    # Agregar campo de clave primaria para la tabla pivote
    class Meta:
        database = database
        db_table = 'product_categories'
        primary_key = peewee.CompositeKey('product', 'category')

# FUNCION MAIN
database.drop_tables([Product, Category, ProductCategory])
database.create_tables([Product, Category, ProductCategory])

ipad = Product.create(title='Ipad', price=500.50)
iphone = Product.create(title="IPhone", price=800.00)
tv = Product.create(title="Tv", price=600.00)

technology = Category.create(title='Technology')
home = Category.create(title='Home')

# Como es una relación muchos a muchos, tenemos que crear una tabla pivote que una a los dos
ProductCategory.create(product=ipad, category=technology)
ProductCategory.create(product=iphone, category=technology)
ProductCategory.create(product=tv, category=technology)

ProductCategory.create(product=tv, category=home)

# Acceder a productos a través de una categoría
#for product_category in ProductCategory.select().where(ProductCategory.category == technology):
#    print(product_category.product)

# Acceder a categorías a través de un producto
#for product_category in ProductCategory.select().where(ProductCategory.product == tv):
#    print(product_category.category)

#Mostrar en consola todos los prodcutos con sus correspodientes categorias!

#Este algoritmo produce el problema N+1 query 
for product in Product.select(): #Aqui hacemos una consulta
    
    for product_categories in product.categories: #Realizamos otra consulta 
        print(product,'-',product_categories.category) #Realizamos otra consulta

        