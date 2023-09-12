import os

def menu_hash_colisions(colisions):
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
            [cualquier valor] - Atras 
            
            Option: """)
        os.system('cls')

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
                return True, "Salida Exitosa"
        except ValueError:
            print("Valor incorrecto por favor intente de nuevo")
    
    return


