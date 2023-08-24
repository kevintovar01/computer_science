from hash_trasformation import HashTrasformation
import os

if __name__ == '__main__':
    
    lenght = int(input("Ingrese el tama;o que desea para la memoria: ")) #thats going to memory to we hash
    my_hash = HashTrasformation(lenght)  # we instance that class, for use the method hash
    
    while True:
        option = input(
            """Selecciones el metodo hash que quiere utilizar 
            para la asignacion de datos a nustra memoria
                [1] - hash mod
                [2] - hash cuadrado
                [3] - hash truncamiento
                [4] - hash plegamiento

            """)
        value = int(input("Ingresa el valor que deseas a;adir a la memoria: "))
        if option == '1':
            my_hash.hash_function(value)
        elif option == '2':
            pass
        elif option == '3':
            pass
        elif option == '4':
            pass
        else:
            os.system('cls')
            print("Por favor ingrese un valor valido")
        


        
        

        