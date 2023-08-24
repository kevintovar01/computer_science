import random

colosiones = []

def hash_truncamiento(value, len_list):
    truncate = ''.join(map(str, [ord(i) for i in value]))
    while True:
        code = [truncate[i] for i in range(len(str(len_list))) if i%2 == 0]
        index = int(''.join(map(str, code))) + 1
        if index >  len_list:
            truncate = value[len(str(len_list)):]
        else:
            break
    return index
    

def insert_with_collision_handling(my_list, value, len_list):
    index = hash_truncamiento(value, len_list) - 1

    if my_list[index] is not None:
        print("presenta colision")
        colosiones.append(value)
    else:
        my_list[index] = value


def search(search_num, my_list):
    index = hash_truncamiento(search_num, len(my_list)) -1

    if my_list[index] == search_num:
        print("El número", search_num, "fue encontrado en la posición", index)
    else:
        print("El número", search_num, "no se encontró en la lista.")


def run():
    len_list = int(input("Ingrese el rango del arreglo: "))
    
    my_list = [None] * len_list
    
    added_numbers = set()
    while len(added_numbers) < len_list:
        
        value = str(random.randint(len_list, 1000))
        
        
        if value not in added_numbers:
            insert_with_collision_handling(my_list, value, len_list)
            added_numbers.add(value)
    
    print("Arreglo completo:")
    print(added_numbers)
    print(my_list)
    print(len(my_list))
    
    while True:
        search_num = input("Ingrese el número a buscar: ")  # Entrada como cadena
        search(search_num, my_list)


if __name__ == '__main__':
    run()