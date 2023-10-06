import os
def conditions():
    os.system('cls')
    while True:
        try:
            cube = int(input("Ingrese tamaño que desea por cubetas multiplo de 2: "))
            if cube % 2 != 0:
                print("Tiene que ser multiplo de 2")
            else:
                break
        except ValueError:
            print("Valor no valido")

    while True:
        try:
            tasa_expansion = int(input("Ingrese tasa_expansion % (recomendacion entre 10 a 80%): "))
            if tasa_expansion >= 90:
                print("La tasa de expansion esta muy alta, esto podria generara error a futuro, por favor cambiar")
            else:
                row = int(input("Ingrese tamaño que desea por filas: "))
                tasa_reduccion = int(input("Ingrese tasa_reduccion %: "))
                break

        except ValueError:
            print("Error, Alparecer has ingrasado un valor no valido para el programa intenta de nuevo")


    return cube, row, tasa_expansion, tasa_reduccion
