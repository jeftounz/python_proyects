import psycopg2

class Registro_datos():

    def __init__(self):
        self.conexion = psycopg2.connect(
            host='localhost',
            port='5432',
            database='base_datos',
            user='postgres',
            password='admin'
        )

    def inserta_producto(self, codigo, nombre, modelo, precio, cantidad):
        cur = self.conexion.cursor()
        sql = '''INSERT INTO productos (CODIGO, NOMBRE, MODELO, PRECIO, CANTIDAD) 
                 VALUES(%s, %s, %s, %s, %s)'''
        values = (codigo, nombre, modelo, precio, cantidad)
        cur.execute(sql, values)
        self.conexion.commit()
        cur.close()

    def mostrar_productos(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM productos"
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def busca_producto(self, nombre_producto):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM productos WHERE NOMBRE = %s"
        cur.execute(sql, (nombre_producto,))
        nombreX = cur.fetchall()
        cur.close()
        return nombreX

    def elimina_productos(self, nombre):
        cur = self.conexion.cursor()
        sql = '''DELETE FROM productos WHERE NOMBRE = %s'''
        cur.execute(sql, (nombre,))
        self.conexion.commit()
        cur.close()
