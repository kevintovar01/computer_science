

#class hash fuctions
from hash_trasformation import HashTrasformation
from hash_colisions import HashColision

#python libraries
import os

def hash_menu(function_hash, name_function, funtion_colision, my_hash):


    range_number = int(input("Primero debes ingresar un rango(digitos) fijo para las claves: "))
    os.system('cls')
    while True:
        option = input(f"""
            Estas utilizando la funcion {name_function}, a continuacion
            tienes las siguientes funciones elije la que desees para
            manipular tu lista(memoria):
              
                [1] - Insertar claves(uno a uno)
                [2] - Insertar lista de claves(varios)
                [3] - busca elementos
                [4] - ver lista(completa)
                [5] - ver valores y claves(los almacenados sola mente)
                [6] - ver elementos con colision
                [7] - ver todo
                [8] - cambiar rango(cantidad digitos)
            [cualquier valor] - salir 
            
            Option: """)
        os.system('cls')
        try: 
            if option == '1':
                while True:
                    value = int(input("Ingrese un valor: "))
                    if len(str(value)) == range_number:
                        break
                    print(f"debe de ser de {range_number} digitos")

                my_hash.insert(value, function_hash, funtion_colision)

            elif option == '2':

                values = list(map(int, input(f"Porfavor insertar las claves de forma horizontal separadas por espacios y de digitos iguales a {range_number}: ").split()))
          
                for i in values:
                    if len(values) > my_hash.lenght:
                        print("Al parecer la lista que tratas de ingresar excede el espacio de memoria, vuelve a intentarlo")
                        break

                    if len(str(i)) == range_number:
                        my_hash.insert(i, function_hash, funtion_colision)
                    else:
                        print(f"Error Alguna clave tiene digitos menores o mayores a {range_number} por favor intente de nuevo")                    

            elif option == '3':
                value = int(input("Ingrese valor que desea buscar: "))
                my_hash.search(value, function_hash, funtion_colision)
            elif option == '4':
                print("Memory: ", my_hash.memory)
            elif option == '5':
                print("valor:clave: ", my_hash.key_value())
            elif option == '6':
                print(f"colisiones {len(my_hash.colisions)}: ", my_hash.colisions)
            elif option == '7':
                my_hash.print_all()
            elif option == '8':
                range_number = int(input("'tener encuenta que al cambiar se rango se reinicia la memoria' ingresa una letra para cancelar, ingrese nuevo rango: ")) 
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