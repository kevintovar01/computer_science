import os

def menu_structures(function_hash, name_function, my_hash, my_structure):
    while True:
        try:
            range_number = int(input("Primero debes ingresar un rango(digitos) fijo para las claves: "))
            break
        except ValueError:
            print("Solo se permiten valores enteros")
    
    os.system('cls')
    while True:
        option = input(f"""
            Estas utilizando la funcion {name_function} para insertar claves, 
            a continuacion tienes las siguientes funciones elije la que desees
            para manipular tu lista(memoria):
              
                [1] - Insertar claves(uno a uno)
                [2] - Insertar lista de claves(varios)
                [3] - Busca elementos
                [4] - Ver lista(completa)
                [5] - Historial de claves
                [6] - Ver elementos con colision
                [7] - Ver todo
                [8] - Cambiar rango(cantidad digitos)
                [9] - Eliminar clave
                [10] - Eliminar Lista
            [cualquier valor] - atras 
            
            Option: """)
        os.system('cls')
        try: 
            if option == '1':
                while True:
                    value = int(input("Ingrese un valor: "))
                    if len(str(value)) == range_number:
                        break
                    print(f"debe de ser de {range_number} digitos")

                value, index = my_hash.insert(value, function_hash)
                my_structure.agregar_clave(index,value)

            elif option == '2':

                values = list(map(int, input(f"Porfavor insertar las claves de forma horizontal separadas por espacios y de digitos iguales a {range_number}: ").split()))
          
                for i in values:
                    if len(str(i)) == range_number:
                        value, index = my_hash.insert(i, function_hash)
                        my_structure.agregar_clave(index,value)
                    else:
                        print(f"Error Alguna clave tiene digitos menores o mayores a {range_number} por favor intente de nuevo")                    

            elif option == '3':
                value = int(input("Ingrese valor que desea buscar: "))
                my_structure.buscar_clave(value)
            elif option == '4':
                my_structure.imprimir_estructura()
            elif option == '5':
                pass
            elif option == '6':
                print(f"colisiones {len(my_structure.lista_colisiones)}: ", my_structure.lista_colisiones)
            elif option == '7':
                my_structure.print_all()
            elif option == '8':
                range_number = int(input("'tener encuenta que al cambiar se rango se reinicia la memoria' ingresa una letra para cancelar, ingrese nuevo rango: ")) 
                my_structure.reset_list()
            elif option == '9':
                value = int(input("Ingrese clave a eliminar: ")) 
                my_structure.eliminar_clave(value)
            elif option == '10':
                my_structure.reset_list()
            else:
                if exit():
                    my_structure.reset_list()
                    return True
        except ValueError:
            print("Error: Valor o lista de claves son incorrectos por favor intente de nuevo")   


def exit():
    option = input(f"""
                    Al salir se eliminara la Estructura ya creada anteriormente ¿Desea continuar? 
                        [cualquier valor] - Continuar
                            [2] - Cancelar
                   
                    elija una opcion: """)
    
    if option == '2':
        return False
    else:
        return True 

    


