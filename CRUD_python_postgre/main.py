import psycopg2

DROP_USERS_TABLE="DROP TABLE IF EXISTS users"

USERS_TABLE="""CREATE TABLE users(id SERIAL,
username VARCHAR(50) NOT NULL,
email VARCHAR(50) NOT NULL,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
"""

def craete_user():
    """A) Crear usuario"""
    print("Usuario creado")

def list_users():
    """B) Listar usuarios"""
    print("Usuario creado")


def upadte_user():
    """C) Actualizar usuario"""
    print("Usuario creado")


def delete_user():
    """D) Eliminar usuario"""
    print("Usuario creado")

def default():
    print("Opcion no valida")

if __name__=="__main__":
    
    options={
        'a':craete_user,
        'b':list_users,
        'c':upadte_user,
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

                option:input("Seleccion una opcion valida:").lower()

                if option=="quit" or option=="q":
                    break

                function=options.get(option,default)
                function()

        connect.close()

    except psycopg2.OperationalError as err:

        print("No fue posble realizar la conexión!")
        print(err)
