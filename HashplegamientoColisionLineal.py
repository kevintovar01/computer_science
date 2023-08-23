import random

N = 100  # Definimos N como 100

def split_into_groups(key, group_size):
    key_str = str(key)
    return [int(key_str[i:i+group_size]) for i in range(0, len(key_str), group_size)]

def hash_function_fold_multiplicative(K):
    group_size = 2  # Dividir en grupos de 2 dígitos
    key_groups = split_into_groups(K, group_size)
    
    hash_value = 1
    for group in key_groups:
        hash_value *= group
    
    hash_value %= N
    
    return (hash_value % N) + 1

def linear_probe(index):
    return (index + 1) % N

def insert_with_collision_handling(array, num):
    index = hash_function_fold_multiplicative(num) - 1
    while array[index] is not None:
        index = linear_probe(index)
    array[index] = num

def main():
    num_count = int(input("Ingrese la cantidad de números a agregar (menor a {}): ".format(N)))
    
    if num_count >= N:
        print("La cantidad de números debe ser estrictamente menor a {}".format(N))
        return
    
    array = [None] * N
    
    added_numbers = set()
    while len(added_numbers) < num_count:
        num = random.randint(N*10, N*100)
        if num not in added_numbers:
            insert_with_collision_handling(array, num)
            added_numbers.add(num)
    
    print("Arreglo completo:")
    print(array)
    
    while True:
        search_num = int(input("Ingrese el número a buscar: "))
        search_index = hash_function_fold_multiplicative(search_num) - 1
        found = False
        for _ in range(N):
            if array[search_index] == search_num:
                print("El número", search_num, "fue encontrado en la posición", search_index + 1)
                found = True
                break
            search_index = linear_probe(search_index)
        if not found:
            print("El número", search_num, "no se encuentra en el arreglo.")
    
if __name__ == "__main__":
    main()
