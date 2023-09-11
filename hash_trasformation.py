from hash_colisions import HashColision

class HashTrasformation:
    def __init__(self, lenght) -> None:
        self.lenght = lenght
        self.memory = [None]*lenght
        self.colisions = []
        self.anidado = [[None for i in range(lenght)] for i in range(lenght)]

    def search(self, value, function_hash, funtion_colision):
        index = function_hash(value) -1

        if self.memory[index] == value:
            print("El número", value, "fue encontrado en la posición", index)
        else:
            index = funtion_colision(self.memory, index, value)        
            print("El número", value, f"fue encontrado en la posición {index}" if index != None else "No se encuentra en la memoria")
    

    def insert(self, value, function_hash, funtion_colision):
        index = function_hash(value)-1

        if not None in self.memory:
            print("Espacio insuficiente")
            return
    
        if self.memory[index] == value:
            print(f'Esta clave "{value}" ya se encuentra en la lista')
            return
        elif self.memory[index] is not None:
            print(f"presenta colision la clave {value}")
            index = funtion_colision(self.memory, index)
            self.memory[index] = value
            self.colisions.append(value)
        else:
            self.memory[index] = value


    def hash_function(self, value): #value --> k and prime_below --> n
        prime_below = self.prime_below()
        return (value % prime_below) + 1
        # self.insert(index, value)


    def hash_function_square(self, value):
        prime_below = self.prime_below()
        squared = value ** 2
        digit_count = len(str(prime_below))

        middle_digits = self.get_middle_digits(squared, digit_count)

        if len(str(middle_digits)) > digit_count:
            middle_digits = int(str(squared)[:digit_count])

        # Si el cuadrado es igual a N, forzamos el dígito izquierdo a 0
        if squared == prime_below:
            middle_digits = int(str(squared)[:1])

        return (middle_digits % prime_below) + 1
        #self.insert(index, value) 


    def hash_function_fold_multiplicative(self, value):
        prime_below = self.prime_below()
        group_size = len(str(prime_below))  # Dividir en grupos con los mismos digitos dependiendo del N ingresado
        key_groups = self.split_into_groups(value, group_size)
        
        hash_value = 1
        for group in key_groups:
            hash_value *= group
        
        hash_value %= self.lenght
        return (hash_value % self.lenght) + 1
        #self.insert(index,value)
        

    def hash_function_fold_additive(self, value):
        prime_below = self.prime_below()
        group_size = len(str(prime_below))  # Dividir en grupos con los mismos digitos dependiendo del N ingresado
        key_groups = self.split_into_groups(value, group_size)
        
        hash_value = 0
        for group in key_groups:
            hash_value += group
        
        # hash_value %= self.memory
        
        return (hash_value % self.lenght) + 1


    #3022 --  32+1 ==33 2230 -- 23+1 =24  234523 -- 242+1
    def hash_truncamiento(self, value):
        element = str(value)
        code = [element[i] for i in range(len(str(self.lenght))) if i%2 == 0]
        index = int(''.join(map(str, code))) + 1
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
        prime = self.lenght
        while not self.is_prime(prime):
            prime -= 1
        return prime
    
    def key_value(self):
        my_dict = {value:self.memory.index(value) for value in self.memory if value != None}
        return my_dict
    
    def print_all(self):
        print("Memory: ", self.memory)
        print(f"Colisiones: {len(self.colisions)}", self.colisions)
        print("valor:clave : ", self.key_value())

    def get_middle_digits(self, num, digit_count):
        num_str = str(num)
        total_digits = len(num_str)

        if digit_count > total_digits:
            raise ValueError("El número de dígitos requeridos es mayor que el número de dígitos en el número.")

        start = (total_digits - digit_count) // 2

        end = start + digit_count

        return int(num_str[start:end])
    
    def split_into_groups(self, key, group_size):
        key_str = str(key)
        return [int(key_str[i:i+group_size]) for i in range(0, len(key_str), group_size)]
    
    def reset_list(self):
        self.memory = []
        self.memory = [None] * self.lenght
