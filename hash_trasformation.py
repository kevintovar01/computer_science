# como hacer un asobre carga de un operador como en un lenguaje c o c++

class HashTrasformation:
    def __init__(self, lenght) -> None:
        self.memory = [None]*lenght
        self.colisions = []

    
    def insert(self, index, value):
        
        if self.memory[index-1] is not None:
            print("presenta colision")
            self.colision.append(value)
        else:
            self.memory[index-1] = value


    def hash_function(self, value): #value --> k and prime_below --> n
        prime_below = self.prime_below()
        index = (value % prime_below) + 1
        self.insert(index)

    def hash_function_square(K):
        squared = K ** 2
        digit_count = len(str(N))
        
        middle_digits = get_middle_digits(squared, digit_count)
        
        if len(str(middle_digits)) > digit_count:
            middle_digits = int(str(squared)[:digit_count])
        
        # Si el cuadrado es igual a N, forzamos el dígito izquierdo a 0
        if squared == N:
            middle_digits = int(str(squared)[:1])
        
        return (middle_digits % N) 


    def hash_function_fold_multiplicative(K):
        group_size = 2  # Dividir en grupos de 2 dígitos
        key_groups = split_into_groups(K, group_size)
        
        hash_value = 1
        for group in key_groups:
            hash_value *= group
        
        hash_value %= N
        
        return (hash_value % N) + 1


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
    

    
    def is_prime(self, num):
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


    def prime_below(self):
        prime = len(self.memory)
        while not self.is_prime(prime):
            prime -= 1
        return prime
    
    def print_list(self):
        print(self.memory)
        print(self.colisions) 
