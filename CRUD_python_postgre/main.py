import psycopg2

DROP_USERS_TABLE="DROP TABLE IF EXISTS users"

USERS_TABLE="""CREATE TABLE users(id SERIAL,
username VARCHAR(50) NOT NULL,
email VARCHAR(50) NOT NULL,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
"""

def create_user(connect,cursor):
    """A) Crear usuario"""
    
    confirm=False
    
    while confirm==False:
        username=input("Ingrese su nombre de usuario: ")
        email=input("Ingrese su email: ")
        if ('@' in email)==True:
            confirm=True  
            print("Porfavor, un email lleva siempre un @")

    query="INSERT INTO users(username, email) VALUES(%s, %s)"
    values=(username,email)

    cursor.execute(query,values)
    connect.commit()

    print(">>>USUARIO CREADO EXITOSAMENTE")
    print("---------------------------")

def list_users(connect,cursor):
    """B) Listar usuarios"""
    query="SELECT id, username, email FROM users"
    cursor.execute(query)

    print(">>>Lista de usuarios:")

    for id, username, email in cursor.fetchall():
        print(id,'-',username,'-',email)

    print("---------------------------")
    


def update_user(connect,cursor):
    """C) Actualizar usuario"""
    id=input("Ingresa el id del usuario a actualizar: ")

    query="SELECT id FROM users WHERE id= %s"
    cursor.execute(query,(id,))

    user=cursor.fetchone() #None
    if user:

        username=input("Ingresa un nuevo username: ")
        email=input("Ingresa un nuevo email: ")

        query="UPDATE users SET username = %s, email= %s WHERE id= %s"
        values=(username, email, id)
        cursor.execute(query, values)
        connect.commit()
        print(">>>USUARIO ACTUALIZADO EXITOSAMENTE")
    else:
        print("No existe un suario con ese id, intente de nuevo!")    



def delete_user(connect,cursor):
    """D) Eliminar usuario"""
    id=input("Ingrese el id del usuario a actualizar")

    query="SELECT id FROM users WHERE id= %s"
    cursor.execute(query,(id,))

    user=cursor.fetchone()
    if user:
        query="DELETE FROM users WHERE id=%s"
        cursor.execute(query,(id,))
        connect.commit()
        print(">>>USUARIO ELIMINADO EXITOSAMENTE")
    else:
        print("No existe un suario con ese id, intente de nuevo!")      
    


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
            
            #cursor.execute(DROP_USERS_TABLE)
            #cursor.execute(USERS_TABLE)

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
