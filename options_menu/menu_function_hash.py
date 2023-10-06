#class functions
from function_hash.hash_trasformation import HashTrasformation

#python libraries
import os




def menu_hash_function(my_hash):
    
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
        
        try:
            if option == '1':
                return functions_hash['hash mod'], 'hash mod'
            elif option == '2':
                return functions_hash['hash cuadrado'], 'hash cuadrado'
            elif option == '3':
                while True:
                    my_hash.order = input(f"Que posicion de digitos le gustaria tomar par o impar: ").lower()
                    if my_hash.order == 'par':
                        my_hash.order = 0
                        break
                    elif my_hash.order == 'impar':
                        my_hash.order = 1
                        break
                    else:
                        print("Valor incorrecto intenta de nuevo")
                return functions_hash['hash truncamiento'], 'hash truncamiento'
            elif option == '4':
                return functions_hash['hash plegamiento multiplicacion'], 'hash plegamiento multiplicacion'
            elif option == '5':
                return functions_hash['hash plegamiento suma'], 'hash plegamiento suma'
            elif option == '6':
                length = int(input("Ingrese el tamaño que desea para la memoria: "))
                my_hash.length = length
                my_hash.reset_list()
            else:        
                os.system('cls')
                return True, "Salida Exitosa"
        except ValueError:
            print("Por favor ingrese un valor valido")