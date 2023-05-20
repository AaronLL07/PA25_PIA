nombres = ["Juan", "María", "Pedro", "Ana"]
archivo = open("todo.txt", "w")

for nombre in nombres:
    archivo.write(nombre + "\n")

archivo.close()

archivo = open("datos.txt", "r")
contenido = archivo.read()
archivo.close()

print(contenido)
