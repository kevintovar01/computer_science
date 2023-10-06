
#python libraries
import os

def hash_menu(function_hash, name_function, funtion_colision, my_hash, name_colision):
    while True:
        try:
            range_number = int(input("Primero debes ingresar un rango(digitos) fijo para las claves: "))
            break
        except ValueError:
            print("Solo se permiten valores enteros")
    
    os.system('cls')
    while True:
        option = input(f"""
            Estas utilizando la funcion {name_function}, a continuacion
            tienes las siguientes funciones elije la que desees para
            manipular tu lista(memoria):
              
                [1] - Insertar claves(uno a uno)
                [2] - Insertar lista de claves(varios)
                [3] - Busca elementos
                [4] - Ver lista(completa)
                [5] - Ver valores y claves(los almacenados sola mente)
                [6] - Ver elementos con colision
                [7] - Ver todo
                [8] - Cambiar rango(cantidad digitos)
                [9] - Eliminar clave
               [10] - Eliminar Lista
            [cualquier valor] - atras 
            
            Opcion: """)
        os.system('cls')
        try: 
            if option == '1':
                while True:
                    value = int(input("Ingrese un valor: "))
                    if len(str(value)) == range_number:
                        break
                    print(f"debe de ser de {range_number} digitos")

                my_hash.insert(value, function_hash, funtion_colision, name_colision)

            elif option == '2':

                values = list(map(int, input(f"Porfavor insertar las claves de forma horizontal separadas por espacios y de digitos iguales a {range_number}: ").split()))
          
                for i in values:
                    if len(values) > my_hash.length:
                        print("Al parecer la lista que tratas de ingresar excede el espacio de memoria, vuelve a intentarlo")
                        break

                    if len(str(i)) == range_number:
                        my_hash.insert(i, function_hash, funtion_colision, name_colision)
                    else:
                        print(f"Error Alguna clave tiene digitos menores o mayores a {range_number} por favor intente de nuevo")                    

            elif option == '3':
                value = int(input("Ingrese valor que desea buscar: "))
                my_hash.search(value, function_hash, funtion_colision)
            elif option == '4':

                if name_colision == 'lista encadenada':
                    print("Memory: ")
                    for i, value in enumerate(my_hash.memory):
                        print(f"[{value}] -> {my_hash.cadena[i]}")
                elif name_colision == 'arreglo anidado':
                    print("Memory: ")
                    for i, value in enumerate(my_hash.memory):
                        print(f"[{value}] -> {my_hash.anidado[i]}")
                else:
                    print("Memory: ", my_hash.memory)

            elif option == '5':
                print("valor:clave: ", my_hash.key_value())
            elif option == '6':
                print(f"colisiones {len(my_hash.colisions)}: ", my_hash.colisions)
            elif option == '7':
                my_hash.print_all(name_colision)
            elif option == '8':
                range_number = int(input("'tener encuenta que al cambiar se rango se reinicia la memoria' ingresa una letra para cancelar, ingrese nuevo rango: ")) 
                my_hash.reset_list()
            elif option == '9':
                value = int(input("Ingrese clave: ")) 
                my_hash.delete(value, function_hash, funtion_colision, name_colision)
            elif option == '10':
                my_hash.reset_list()
            else:
                if exit():
                    my_hash.reset_list()
                    return True
        except ValueError:
            print("Error: Valor o lista de claves son incorrectos por favor intente de nuevo")
    
    


def exit():
    option = input(f"""
                    Al salir se eliminara la lista ya creada anteriormente ¿Desea continuar? 
                        [cualquier valor] - Continuar
                            [2] - Cancelar
                   
                    elija una opcion: """)
    
    if option == '2':
        return False
    else:
        return True 