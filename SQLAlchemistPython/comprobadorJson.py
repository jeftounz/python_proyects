import json
#ESTE ARCHIVO ES PARA COMPROBAR COMO FUNCIONA 
with open("usuarios.json", "r") as file:
    try:
        data = json.load(file)
        print(data)
    except json.JSONDecodeError:
        print("No se pudo decodificar el JSON. Asegúrate de que el archivo JSON sea válido.")
    except FileNotFoundError:
        print("El archivo 'data.json' no fue encontrado.")
