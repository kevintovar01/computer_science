#menu
from options_menu.hash_menu import hash_menu

from function_hash.hash_trasformation import HashTrasformation
from function_hash.hash_colisions import HashColision

#menu hashs
from options_menu.menu_function_hash import menu_hash_function
from options_menu.menu_colisions import menu_hash_colisions

from options_menu.menu_memory import menu_memory
from options_menu.menu_structures import menu_structures 


if __name__ == '__main__':
    try:
        length, structure = menu_memory()
        if structure == 'Estructura parcial' or structure == 'Estructura total':
            my_hash = HashTrasformation(0, True)
            my_structure = length
            pass
        else:
            my_hash = HashTrasformation(length)
            hash_colisions = HashColision(my_hash)

        while True:
            
            function_hash, name_function = menu_hash_function(my_hash)

            if function_hash == True:
                print(name_function)
                break

            if structure == 'Estructura parcial' or structure == 'Estructura total':
                my_structure.function_hash = function_hash
                my_structure.my_hash = my_hash
                menu_structures(function_hash, name_function, my_hash, my_structure)
            else:    
                funtion_colision, name_colision = menu_hash_colisions(hash_colisions)
                
                if funtion_colision != True:
                    hash_menu(function_hash, name_function, funtion_colision, my_hash, name_colision)  
    except:
        print("Salida Exitosa")