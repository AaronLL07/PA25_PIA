from clase_frase import Frase

frases = []

opcion = 0
total_op = 0 # contador de opiniones
fr_ag = 0 # variable para poder entrar en la condición en caso de que ya haya una frase ingresada
cont = 0 # acumulador para ir contando las estrellas para sacar promedio de 5 estrellas
while opcion != 6:
    print("Bienvenidos")
    print("1.- Agregar frase\n2.- Ver frase\n3.- Ver todas las frases\n4.- Eliminar frase\n5.- Modificar frase\n6.- Salir")
    opcion = int(input("Seleccione la opción deseada: "))

    if opcion == 1:
        stars_calif = [0, 0, 0, 0, 0]
        if fr_ag == 0:
            print(7*"*", "Agregar frase", 7*"*")
            id_frase = int(input("Ingrese el ID de la frase: "))
            frase = input("Ingrese la frase motivadora que desea agregar: ")
            autor = input("Autor de la frase: ")
            obj_frase = Frase(id_frase, frase, autor, stars_calif)
            frases.append(obj_frase)
            fr_ag += 1

        elif fr_ag > 0:
            id_frase = -1
            while obj_frase.id_frase != id_frase:
                print(7*"*", "Agregar frase", 7*"*")
                id_frase = int(input("Ingrese el ID de la frase: "))
                if obj_frase.id_frase != id_frase:
                    frase = input("Ingrese la frase motivadora que desea agregar: ")
                    autor = input("Autor de la frase: ")
                    obj_frase = Frase(id_frase, frase, autor, stars_calif)
                    frases.append(obj_frase)
                    break
                if obj_frase.id_frase == id_frase:
                    print("Ya se encuentra una frase con ese ID, intente con un ID distinto.")
                    id_frase = -1
   
    elif opcion == 2:
        
        print(7*"*", "Ver frase", 7*"*")
        id_frase = -1
        while obj_frase.id_frase != id_frase:
            id_frase = int(input("Ingrese el ID de la frase que desea ver y calificar: "))
            for obj_frase in frases:
                if obj_frase.id_frase == id_frase:                    
                    obj_frase.info_frase()
                    print(21*"*")
                    total_op +=1  # contador del total de opiniones 
                    break
                          
            if obj_frase.id_frase != id_frase:
                print("No coincide el ID con ninguna frase almacenada, ingrese el ID de nuevo.")
        
        estrella = 0
        while estrella < 1 or estrella > 5:
            estrella = int(input("Califica la frase de 1 a 5 estrellas: "))
            cont += estrella
            stars_calif[estrella - 1] += 1
            if estrella < 1 or estrella > 5:
                print("Ingrese una calificación válida, 1 a 5 estrellas.")  

        for i in range (1, 6):
            cant = stars_calif[i-1]
            porcentaje = (cant / total_op) * 100
            resultado = (i, porcentaje)
            stars_calif.append(resultado)
        
        res = input("Desea ver la calificación que acaba de ingresar S/N: ")    
        if res.upper() == "S":
            print(f"{total_op} calificaciones globales")
            obj_frase.mostrar_frase()
        elif res.upper() == "N":
            print("Podrá ver su calificación luego.")

    elif opcion == 3:
        print(7*"*", "Ver todas las frases", 7*"*")
        for obj_frase in frases:
            obj_frase.mostrar_frase()

    elif opcion == 4:
        print(7*"*", "Eliminar frase", 7*"*")
        id_frase = -1
        while obj_frase.id_frase != id_frase:
            id_frase = int(input("Ingrese el ID de la frase que eliminar: "))
            for obj_frase in frases:
                if obj_frase.id_frase == id_frase:
                    frases.remove(obj_frase)
                    break
            if obj_frase.id_frase != id_frase:
                print("No coincide el ID con ninguna frase almacenada, ingrese el ID de nuevo.")

    elif opcion == 5:
        id_frase = -1
        while obj_frase.id_frase != id_frase:
            id_frase = int(input("Ingrese el ID de la frase modificar: "))
            if obj_frase.id_frase == id_frase:     
                for obj_frase in frases:
                    nueva_frase = input("Ingrese la frase con la que desea remplazar la anterior: ")
                    nuevo_autor = input("Ingrese el nombre del autor para modificar el anterior: ")
                    obj_frase.frase = nueva_frase
                    obj_frase.autor = nuevo_autor
        if obj_frase.id_frase != id_frase:
                print("No coincide el ID con ninguna frase almacenada, ingrese el ID de nuevo.")

    elif opcion == 6:
        print("¡Hasta pronto!")