import random

colisiones = []
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def find_nearest_prime_below(n):
    while not is_prime(n):
        n -= 1
    return n

def hash_function(K, N):
    return (K % N) + 1


def insert_with_collision_handling(my_list, value, prime_below_N):
    index = hash_function(value, prime_below_N) - 1
    if my_list[index] is not None:
        print("presenta colision")
        colisiones.append(value)
    else:
        my_list[index] = value

def search(search_num, my_list, prime_below_N):
    index = hash_function(search_num, prime_below_N) - 1

    if my_list[index] == search_num:
        print("El número", search_num, "fue encontrado en la posición", index)
    else:
        print("El número", search_num, "no se encontró en la lista.")

def main():
    N = int(input("Ingrese el rango del arreglo: "))
    prime_below_N = find_nearest_prime_below(N)
    print("El número primo más cercano por debajo de", N, "es:", prime_below_N)
    
    array = [None] * N
    
    num_count = prime_below_N
    added_numbers = set()
    while len(added_numbers) < num_count:
        num = random.randint(N, 1000)
        if num not in added_numbers:
            insert_with_collision_handling(array, num, prime_below_N)
            added_numbers.add(num)
    
    print("Arreglo completo:")
    print(array)
    
    while True:
        search_num = int(input("Ingrese el número a buscar: "))
        search(search_num,array, prime_below_N)
    
if __name__ == "__main__":
    main()