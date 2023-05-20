frases = []

opcion = 0
while opcion != 6:
    print("Bienvenidos")
    print("1.- Agregar frase\n2.- Ver frase\n3.- Ver todas las frases\n4.- Eliminar frase\n5.- Modificar frase\n6.- Salir")
    opcion = int(input("Seleccione la opción deseada: "))

    if opcion == 1:
        print(7*"*", "Agregar frase", 7*"*")
        id_frase = int(input("Ingrese el ID de la frase: "))
        frase = input("Ingrese la frase motivadora que desea agregar: ")
        archivo = open("frases.txt", "a")
        archivo.write("\n" + frase)
        archivo.close()

    elif opcion == 2:
        print(7*"*", "Ver frase", 7*"*")

    elif opcion == 6:
        print("¡Hasta pronto!")
