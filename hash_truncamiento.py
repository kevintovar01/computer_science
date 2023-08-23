import random

def hash_truncamiento(value, len_list):
    truncate = ''.join(map(str, [ord(i) for i in value]))
    code = [truncate[i] for i in range(len(str(len_list))) if i%2 == 0]
    index = int(''.join(map(str, code))) + 1

    return index
    

def insert_with_collision_handling(my_list, value, len_list):
    index = hash_truncamiento(value, len_list) - 1
    while my_list[index] is not None:
        index = (index + 1) % len(my_list)
    my_list[index] = value

def search(search_num, my_list):
    index = hash_truncamiento(search_num, len(my_list))
    original_index = index
    while my_list[index] is not None:
        if my_list[index] == search_num:
            print("El número", search_num, "fue encontrado en la posición", index)
            return
        index = (index + 1) % len(my_list)
        if index == original_index:
            break
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