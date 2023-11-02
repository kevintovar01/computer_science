from function_hash.hash_colisions import HashColision

"""
    In this project, the list or memory start from zero to N-1,
    in the documentacion or example, it is intended(destinado) for a list from one to N
"""
class HashTrasformation:
    def __init__(self, length, memory=None) -> None:
        self.length = length
        self.memory = [None]*length if memory == None else memory
        self.colisions = set({})
        self.anidado = [[None for i in range(length)] for i in range(length)]
        self.cadena =  {i:[] for i in range(length)}
        self.key = None
        self.prime = self.prime_below() #value --> k and prime_below --> n
        self.order = None
        
        


    def search(self, value, function_hash, funtion_colision=None):
        print(value)
        index = function_hash(value) -1

        if self.memory[index] == value:
            print("El número", value, "fue encontrado en la posición", index)
            return value, index, f"El número {value} fue encontrado en la posición {index+1}"
        else:
            index = funtion_colision(self.memory, index, value)     
            print("El número", value, f"fue encontrado en la posición {index+1}" if index != None else "No se encuentra en la memoria")

        return value, index, f"El número {value} fue encontrado en la posición {index+1}" if index != None else "No se encuentra en la memoria"


    def insert(self, value, function_hash, funtion_colision=None, name_colision=None):     
        index = function_hash(value)-1
        self.key = value

        if self.memory == True:
            return None, value, index

        
        if name_colision == 'arreglo anidado' or name_colision == 'lista encadenada' and not None in self.memory:
            funtion_colision(self.memory, index)
            return f"presenta colision la clave {value}", None, None
        elif  not None in self.memory:
            return "Espacio insuficiente", None, None
        #pruebas saber si no solamente vesirica las colisicones
        if self.memory[index] == value or value in self.colisions:
            return f'Esta clave "{value}" ya se encuentra en la lista',None, None
        
        elif self.memory[index] is not None:
            index = funtion_colision(self.memory, index)
            if index != None: 
                self.memory[index] = value
            self.colisions.add(value)
            return f"presenta colision la clave {value}", None, None 
        else:
            self.memory[index] = value
            return None, None, None
    

    def delete(self, value, function_hash, funtion_colision, name_colision):
        value, index, message = self.search(value, function_hash, funtion_colision)

        if index == None:
            return None
        
        if name_colision == 'arreglo anidado':
            try:
                self.anidado[index].remove(value)
                self.anidado[index].append(None)
            except:
                if self.anidado[index] != None:
                    self.memory[index] = self.anidado[index][0]
                    self.anidado[index][0] = None
                else:
                    self.memory[index] = None  
        elif name_colision == 'lista encadenada':
            try:
                self.cadena[index].remove(value)
            except:
                if len(self.cadena[index]) > 0:
                    self.memory[index] = self.cadena[index][0]
                    self.cadena[index].pop(0)
                else:
                    self.memory[index] = None               
        else:
            self.memory[index] = None

        return f"Clave {value} eliminado"

    """
        Modulo Hash Funtion: division  The formula: H(K) = (K mod N) + 1
        N should be the nearest(mas cercano) prime(N size of the array)    
    """
    def hash_function(self, value): 
        return (value % self.prime) + 1 #H(K) = (K mod N) + 1


    """
        Hash Fuction Square the formula: H(K) = central_digits(K^2)+1,
        it consists of squaring keys, then selecting the central numbers and
        adding(sumarle) one at the end. example:
    
        N = 100 K = 7256
        H(K) = central_digits(526"93"081)+1 = 94
    """
    def hash_function_square(self, value):
       
        squared = value ** 2
        digit_count = len(str(self.prime))

        middle_digits = self.get_middle_digits(squared, digit_count)

        if len(str(middle_digits)) > digit_count:
            middle_digits = int(str(squared)[:digit_count])

        # Si el cuadrado es igual a N, forzamos el dígito izquierdo a 0
        if squared == self.prime:
            middle_digits = int(str(squared)[:1])

        return (middle_digits % self.prime) + 1


    """
        Fold Hash Fuction the fomule: H(K) = digmensig([k]/2) + 1

        example: 
        N = 100 K = 7259
        H(K) = digmensig(72 + 59) + 1 --> = (digmensig(131) + 1 = 32
        
        only two digits are taken for the result
        and the same used multiplication

    """
    def hash_function_fold_multiplicative(self, value):
        key_groups = self.split_into_groups(value)
        hash_value = 1
        for group in key_groups:
            hash_value *= group
     
        return (hash_value % self.length) + 1
        

    def hash_function_fold_additive(self, value): 
        groups = self.split_into_groups(value)
        return (sum(groups) % self.length) + 1

    """
        Hash Function consist in taking certain digits of the value and 
        form a key, the formula is: H(K) = select_digits(d1, d2, .. dn)

        The selection of these digits must be even and odd

        Example:
            H(K) = select_digits(7259) + 1 = 75+1 = 76 - odd digits 
                            or
            H(K) = select_digits(7259) + 1 = 29+1 = 30 - even digits
    """
    def hash_truncamiento(self, value):
        element = str(value)

        aux = len(str(self.length))+1
        if len(element) <= len(str(self.length)):
            aux = len(element)

        code = [element[i] for i in range(aux) if i%2 == self.order]
        index = int(''.join(map(str, code))) + 1
        return index

    """
        separate the value(Key) into groups of two using list comprehension and the 'range'
        fuction to go through the length in steps of 2.
    """
    def split_into_groups(self, key):
        key = str(key)
        prime_length = len(str(self.prime))
        even = prime_length
        groups = [int(key[i:i+even]) for i in range(0, len(key), even)] #range: 0-2-4..., i:i+1 = 0-1,2-3,4-5...
        return groups
    

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
        prime = self.length if self.length != 0 else 2
        while not self.is_prime(prime):
            prime -= 1
        return prime
    
    def key_value(self):
        my_dict = {value:self.memory.index(value) for value in self.memory if value != None}
        return my_dict
    

    def print_all(self, name_colision):
        if name_colision == 'lista encadenada':
            print("Memory: ")
            for i, value in enumerate(self.memory):
                print(f"[{value}] -> {self.cadena[i]}")
        elif name_colision == 'arreglo anidado':
            print("Memory: ")
            for i, value in enumerate(self.memory):
                print(f"[{value}] -> {self.anidado[i]}")
            # print("Memory: ", self.anidado)
        else:
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
        
        if (total_digits % 2) == 0 and (digit_count % 2) == 1:
            return int(num_str[start:end+1])
        else:
            return int(num_str[start:end])
    
        
    

    def reset_list(self):
        if self.memory == True:
            self.__init__(self.length, self.memory)
        else:
            aux = self.order
            self.__init__(self.length)
            self.order = aux            