from hash_trasformation import HashTrasformation
import os

def hash_fuction(function_hash, name_function, my_hash):
    os.system('cls')
    while True:
        option = input(f"""
            \nEstas utilizando la funcion {name_function}, a continuacion
            tienes las siguientes funciones elije la que desees para
            manipular tu lista(memoria):
              
                [1] - Insertar datos
                [2] - busca elementos
                [3] - ver list(completa)
                [4] - ver valores y posiciones(los almacenados sola mente)
                [5] - ver elementos con colision
                [6] - salir
            
            Option: 
            """)
        
        if option == '1':
            value = int(input("Ingrese un valor: "))
            my_hash.insert(value, function_hash)
        elif option == '2':
            value = int(input("Ingrese valor que desea buscar: "))
            my_hash.search(value, function_hash)






if __name__ == '__main__':
    
    lenght = int(input("Ingrese el tama;o que desea para la memoria: ")) #thats going to memory to we hash
    my_hash = HashTrasformation(lenght)  # we instance that class, for use the method hash
    
    functions_hash = {
        'hash mod': my_hash.hash_function,
        'hash cuadrado': my_hash.hash_function_square,
        'hash truncamiento': my_hash.hash_truncamiento,
        'hash plegamiento': my_hash.hash_function_fold_multiplicative
    }

    while True:
        option = input(
            """
            \n
            Seleccione el metodo hash que quiere utilizar 
            para la asignacion de datos a nustra memoria
                [1] - hash mod
                [2] - hash cuadrado
                [3] - hash truncamiento
                [4] - hash plegamiento

            Opcion: """)

        if option == '1':
            hash_fuction(functions_hash['hash mod'], 'hash mod', my_hash)
        elif option == '2':
            pass
        elif option == '3':
            pass
        elif option == '4':
            pass
        else:
            os.system('cls')
            print("Por favor ingrese un valor valido")
        


        
        

        