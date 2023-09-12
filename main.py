#menu
from hash_menu import hash_menu

from hash_trasformation import HashTrasformation
from hash_colisions import HashColision

#menu hashs
from menu_function_hash import menu_hash_function
from menu_colisions import menu_hash_colisions          


if __name__ == '__main__':
    
    lenght = int(input("Ingrese el tamaño que desea para la memoria: ")) #thats going to memory to we hash
    my_hash = HashTrasformation(lenght)
    hash_colisions = HashColision(my_hash)

    while True:
        
        function_hash, name_function = menu_hash_function(my_hash)

        if function_hash == True:
            print(name_function)
            break
        
        funtion_colision, name_colision = menu_hash_colisions(hash_colisions)
        
        if funtion_colision != True:
            hash_menu(function_hash, name_function, funtion_colision, my_hash, name_colision)
 
        


        
        

        