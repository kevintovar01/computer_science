from hash_trasformation import HashTrasformation
import os

def hash_fuction(function_hash, name_function, my_hash):
    range_number = int(input("Primero debes ingresar un rango fijo para las claves: "))
    os.system('cls')
    while True:
        option = input(f"""
            Estas utilizando la funcion {name_function}, a continuacion
            tienes las siguientes funciones elije la que desees para
            manipular tu lista(memoria):
              
                [1] - Insertar datos
                [2] - busca elementos
                [3] - ver list(completa)
                [4] - ver valores y claves(los almacenados sola mente)
                [5] - ver elementos con colision
                [6] - ver todo
                [7] - cambiar rango(cantidad digitos)
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

                my_hash.insert(value, function_hash)
            elif option == '2':
                value = int(input("Ingrese valor que desea buscar: "))
                my_hash.search(value, function_hash)
            elif option == '3':
                print("Memory: ", my_hash.memory)
            elif option == '4':
                print("valor:clave: ", my_hash.key_value())
            elif option == '5':
                print(f"colisiones {len(my_hash.colisions)}: ", my_hash.colisions)
            elif option == '6':
                my_hash.print_all()
            elif option == '7':
                range_number = int(input("'tener encuenta que al cambiar se rango se reinicia la memoria' ingresa una letra para cancelar, ingrese nuevo rango: ")) 
                my_hash.reset_list()
            else:
                my_hash.reset_list()
                break
        except ValueError:
            print("Valor incorrecto por favor intente de nuevo")
    
    return 


if __name__ == '__main__':
    
    lenght = int(input("Ingrese el tama;o que desea para la memoria: ")) #thats going to memory to we hash
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
                [6] - cambia el tama;o de tu lista
            [cualquier valor] - salir 

            Opcion: """)
        os.system('cls')
        try:
            if option == '1':
                hash_fuction(functions_hash['hash mod'], 'hash mod', my_hash)
            elif option == '2':
                hash_fuction(functions_hash['hash cuadrado'], 'hash cuadrado', my_hash)
            elif option == '3':
                hash_fuction(functions_hash['hash truncamiento'], 'hash truncamiento', my_hash)
            elif option == '4':
                hash_fuction(functions_hash['hash plegamiento multiplicacion'], 'hash plegamiento multiplicacion', my_hash)
            elif option == '5':
                hash_fuction(functions_hash['hash plegamiento suma'], 'hash plegamiento suma', my_hash)
            elif option == '6':
                lenght = int(input("Ingrese el tama;o que desea para la memoria: "))
                my_hash.lenght = lenght
                my_hash.reset_list()
            else:        
                os.system('cls')
                print('salida exitosa')
                break
        except ValueError:
            print("Por favor ingrese un valor valido")
            
        


        
        

        