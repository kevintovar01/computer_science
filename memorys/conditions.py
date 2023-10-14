import os
def conditions():
    os.system('cls')
    while True:
        try:
            cube = int(input("Ingrese tamaño que desea por cubetas multiplo de 2: "))
            if cube % 2 != 0 or cube <2:
                os.system('cls')
                print("Tiene que ser multiplo de 2, y mayor que 2")
            else:
                break
        except ValueError:
            os.system('cls')
            print("Valor no valido")

    while True:
        try:
            tasa_expansion = int(input("Ingrese tasa_expansion % (recomendacion entre 10 a 80%): "))
            tasa_reduccion = int(input("Ingrese tasa_reduccion %: "))
            row = int(input("Ingrese tamaño que desea por filas: "))
            if tasa_expansion >= 90 or tasa_expansion < 0:
                print("La tasa de expansion esta muy alta, esto podria generara error a futuro, por favor cambiar")
            elif tasa_reduccion < 0:
                print("La tasa de reduccion no es valida, porfavor intenta de nuevo")
            elif row < 1:
                print("El valor que intentas ingresar es incorrecto, intenta con un valor mayor a 1")
            else:
                break
            

        except ValueError:
            os.system('cls')
            print("Error, Alparecer has ingresado un valor no valido para el programa intenta de nuevo")


    return cube, row, tasa_expansion, tasa_reduccion
