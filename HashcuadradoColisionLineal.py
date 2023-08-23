import random

def get_middle_digits(num, digit_count):
    num_str = str(num)
    total_digits = len(num_str)
    
    if digit_count > total_digits:
        raise ValueError("El número de dígitos requeridos es mayor que el número de dígitos en el número.")
    
    start = (total_digits - digit_count) // 2
    
    if total_digits % 2 == 1 and digit_count % 2 == 0:
        start -= 1  # Restar 1 en lugar de sumar 1
    
    end = start + digit_count
    
    return int(num_str[start:end])

def hash_function_square(K):
    squared = K ** 2
    digit_count = len(str(N))
    
    middle_digits = get_middle_digits(squared, digit_count)
    
    if len(str(middle_digits)) > digit_count:
        middle_digits = int(str(squared)[:digit_count])
    
    # Si el cuadrado es igual a N, forzamos el dígito izquierdo a 0
    if squared == N:
        middle_digits = int(str(squared)[:1])
    
    return (middle_digits % N) + 1

def linear_probe(index):
    return (index + 1) % N

def insert_with_collision_handling(array, num):
    index = hash_function_square(num) - 1
    while array[index] is not None:
        index = linear_probe(index)
    array[index] = num

N = 100  # Definimos N como 100

def main():
    num_count = int(input("Ingrese la cantidad de números a agregar (menor a {}): ".format(N)))
    
    if num_count > N:
        print("La cantidad de números debe ser estrictamente menor a {}".format(N))
        return
    
    array = [None] * N
    
    added_numbers = set()
    while len(added_numbers) < num_count:
        num = random.randint(N, N*10)
        if num not in added_numbers:
            insert_with_collision_handling(array, num)
            added_numbers.add(num)
    
    print("Arreglo completo:")
    print(array)
    
    while True:
        search_num = int(input("Ingrese el número a buscar: "))
        search_index = hash_function_square(search_num) - 1
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
