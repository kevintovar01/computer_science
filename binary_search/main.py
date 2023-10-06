from function_hash.binary_search import binary_search
from function_hash.bubble_sort import bubble_sort
from sequence_search import sequence_search
import random
import os

def run():
    my_list = []
    
    lenght = int(input("Ingrese el tamaño que desea para la lista: "))
    while True:
        print(my_list)
        option = input(
            """
            \n
            Seleccione el metodo hash que quiere utilizar 
            para la asignacion de datos a nustra memoria
                [1] - crear o cambia lista random
                [2] - crea o cambia tu propia lista
                [3] - Usa busqueda binaria para buscar un elemento
                [4] - Usa busqueda secuencial para buscar un elemento
                [5] - Ordena la lista
            [cualquier valor] - salir 

            Opcion: """)
        
        os.system('cls')
        try:
            if option == '1':
                my_list = [random.randint(1, 100) for i in range(lenght)]
            elif option == '2':
                my_list = [input(f"Clave #{i}: ") for i in range(lenght)]
            elif option == '3':
                my_list = bubble_sort(my_list)
                objective = int(input("Que valor quieres buscar: "))
                result = binary_search(my_list, objective)
                print(f"result found, objective: {objective}" if result != -1 else "result not found"  )
                
            elif option == '4':
                    objective = int(input("Que valor quieres buscar: "))
                    result = sequence_search(my_list, objective)
                    print(f"result found, objective: {objective}" if result != -1 else "result not found"  )
            elif option == '5':
                my_list = bubble_sort(my_list)
            else:        
                os.system('cls')
                print('salida exitosa')
                break
        except ValueError:
            print("Por favor ingrese un valor valido")
    


if __name__ == '__main__':
    run()