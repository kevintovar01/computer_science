from hash_trasformation import HashTrasformation
from hash_colisions import HashColision
import os

def hash_fuction(function_hash, name_function, my_hash, funtion_colision):
    range_number = int(input("Primero debes ingresar un rango fijo para las claves: "))
    os.system('cls')
    while True:
        option = input(f"""
            Estas utilizando la funcion {name_function}, a continuacion
            tienes las siguientes funciones elije la que desees para
            manipular tu lista(memoria):
              
                [1] - Insertar claves(uno a uno)
                [2] - Insertar lista de claves(varios)
                [3] - busca elementos
                [4] - ver list(completa)
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
                    break
        except ValueError:
            print("Error: Valor o lista de claves son incorrectos por favor intente de nuevo")
    
    return

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
            



def menu_hash_colisions():
    os.system('cls')
    while True:
        option = input(f"""
            En caso de que presente alguna colision, que metodo de solicion
            de colisiones le gustaria usar:
              
                [1] - colision lineal
                [2] - colision cuadratica
                [3] - doble direccion hash
                [4] - arreglo anidado
                [5] - lista encadenada
            [cualquier valor] - salir 
            
            Option: """)
        os.system('cls')
        colisions = HashColision()

        colision_hash = {
            'colision lineal': colisions.lineal_colision,
            'colision cuadreatica': colisions.square_colision,
            'doble direccion hash': colisions.doble_direccion_hash,
            'arreglo anidado': colisions.arreglo_anidado,
            'lista encadenada': colisions.lista_encadenada
        }

        try: 
            if option == '1':
                return colision_hash['colision lineal'], 'colision lineal'
            elif option == '2':
                return colision_hash['colision cuadreatica'], 'colision cuadreatica'
            elif option == '3':
                return colision_hash['doble direccion hash'], 'doble direccion hash'
            elif option == '4':
                return colision_hash['arreglo anidado'], 'arreglo anidado'
            elif option == '5':
                return colision_hash['lista encadenada'], 'lista encadenada'
            else:
                my_hash.reset_list()
                break
        except ValueError:
            print("Valor incorrecto por favor intente de nuevo")
    
    return


 


if __name__ == '__main__':
    
    lenght = int(input("Ingrese el tamaño que desea para la memoria: ")) #thats going to memory to we hash
    my_hash = HashTrasformation(lenght)  # we instance that class, for use the method hash
    
    functions_hash = {
        'hash mod': my_hash.hash_function,
        'hash cuadrado': my_hash.hash_function_square,
        'hash truncamiento': my_hash.hash_truncamiento,
        'hash plegamiento multiplicacion': my_hash.hash_function_fold_multiplicative,
        'hash plegamiento suma': my_hash.hash_function_fold_additive
    }
    os.system('cls')

    while True:
        option = input(
            """
            \n
            Seleccione el metodo hash que quiere utilizar 
            para la asignacion de datos a nustra memoria
                [1] - hash mod
                [2] - hash cuadrado
                [3] - hash truncamiento
                [4] - hash plegamiento multiplicacion
                [5] - hash plegamiento suma
                [6] - cambia el tamaño de tu lista
            [cualquier valor] - salir 

            Opcion: """)
        os.system('cls')
        funtion_colision, text = menu_hash_colisions()
        try:
            if option == '1':
                hash_fuction(functions_hash['hash mod'], 'hash mod', my_hash, funtion_colision)
            elif option == '2':
                hash_fuction(functions_hash['hash cuadrado'], 'hash cuadrado', my_hash, funtion_colision)
            elif option == '3':
                hash_fuction(functions_hash['hash truncamiento'], 'hash truncamiento', my_hash, funtion_colision)
            elif option == '4':
                hash_fuction(functions_hash['hash plegamiento multiplicacion'], 'hash plegamiento multiplicacion', my_hash, funtion_colision)
            elif option == '5':
                hash_fuction(functions_hash['hash plegamiento suma'], 'hash plegamiento suma', my_hash, funtion_colision)
            elif option == '6':
                lenght = int(input("Ingrese el tamaño que desea para la memoria: "))
                my_hash.lenght = lenght
                my_hash.reset_list()
            else:        
                os.system('cls')
                print('salida exitosa')
                break
        except ValueError:
            print("Por favor ingrese un valor valido")
            
        


        
        

        