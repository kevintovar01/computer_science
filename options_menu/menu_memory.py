import os
from memorys.EstructurasParciales import Est_Parcial
from memorys.conditions import conditions



def menu_memory():
    while True:
        os.system('cls')
        option = input(f"""
            Que tipo de memoria deseas utilizar para guardar tus claves:
                       
                [1]-Estructura Totales
                [2]-Estructura parciales
                [3]-Estandar(tipo lista)
            [Cualquier otro valor]-salir     
            
            Opcion: """)
        
        try:
            if option == '1':
                cube, row, tasa_expansion, tasa_reduccion = conditions()
                return Est_Parcial(cube, row, tasa_expansion, tasa_reduccion, "Estructura total"), 'Estructura total'
            elif option == '2':
                cube, row, tasa_expansion, tasa_reduccion = conditions()
                return Est_Parcial(cube, row, tasa_expansion, tasa_reduccion, "Estructura parcial"), 'Estructura parcial'
            elif option == '3':
                while True:
                    return int(input("Ingrese el tamaño que desea para la memoria: ")) #thats going to memory to we hash
            else:        
                os.system('cls')
                return True, "Salida Exitosa"
        except ValueError:
            print("Por favor ingrese un valor valido")
