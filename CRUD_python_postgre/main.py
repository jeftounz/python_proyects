import psycopg2

DROP_USERS_TABLE="DROP TABLE IF EXISTS users"

USERS_TABLE="""CREATE TABLE users(id SERIAL,
username VARCHAR(50) NOT NULL,
email VARCHAR(50) NOT NULL,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
"""

def create_user(connect,cursor):
    """A) Crear usuario"""
    username=input("Ingrese su nombre de usuario: ")
    email=input("Ingrese su email: ")

    query="INSERT INTO users(username, email) VALUES(%s, %s)"
    values=(username,email)

    cursor.execute(query,values)
    connect.commit()

def list_users(connect,cursor):
    """B) Listar usuarios"""
    print("Usuario creado")


def update_user(connect,cursor):
    """C) Actualizar usuario"""
    print("Usuario creado")


def delete_user(connect,cursor):
    """D) Eliminar usuario"""
    print("Usuario creado")

def default(*args):
    print("Opcion no valida")

if __name__=="__main__":
    
    options={
        'a':create_user,
        'b':list_users,
        'c':update_user,
        'd':delete_user
    }

    try:
        connect=psycopg2.connect("postgresql://postgres:admin@localhost/project_pythondb")
        
        with connect.cursor() as cursor:
            
            cursor.execute(DROP_USERS_TABLE)
            cursor.execute(USERS_TABLE)

            connect.commit()

            while True:

                for function in options.values():
                    print(function.__doc__)
                
                print("quit para salir")

                option=input("Seleccion una opcion valida:").lower()

                if option=="quit" or option=="q":
                    break

                function=options.get(option,default)
                function(connect,cursor)

        connect.close()

    except psycopg2.OperationalError as err:

        print("No fue posble realizar la conexión!")
        print(err)
