from binary_search import binary_search 


class HashColision:

    def __init__(self, my_hash) -> None:
        self.my_hash = my_hash
        self.length = self.my_hash.length
    
    
    def lineal_colision(self, memory, index, value=None):
        aux = index

        for i in range(self.length):
            if value != None and value == memory[(aux+i)%self.length]:
                return (aux+i)%self.length
            elif memory[(aux+i)%self.length] is None and value == None:
                return (aux+i)%self.length
    

    def square_colision(self, memory, index, value=None):
        aux = index
        for i in range(1, self.length):                
            if value != None and value == memory[(aux+(i**2))%self.length]:
                return (aux+(i**2))%self.length
            elif memory[(aux+(i**2))%self.length] is None and value == None:
                return (aux+(i**2))%self.length
        return self.lineal_colision(memory, index, value)

    """change that function don't respect : Don't repeat youself"""
    def doble_direccion_hash(self, memory, index, value=None):
        aux = 0
        while value != None:
            aux += 1
            if aux > self.length:
                return self.lineal_colision(memory, index, value)
            
            index = (((index + 1)%self.length)+1)%self.length     
            if value ==  memory[index]:
                return index

        while memory[index] is not None:
            aux += 1
            if aux > self.length:
                return self.lineal_colision(memory, index, value)
            index = (((index + 1)%self.length)+1)%self.length

        return index


    def arreglo_anidado(self, memory, index, value=None):
        if value == None:
            for i in range (len(memory)):
                if self.my_hash.anidado[index][i] is None:
                    self.my_hash.anidado[index][i] = self.my_hash.key
                    break
        else:
            value = binary_search(self.my_hash.anidado[index], value)
            return index
            

    def lista_encadenada(self, memory, index, value=None):
        if value == None:
            self.my_hash.cadena[index].append(self.my_hash.key)
        else:
            result = binary_search(self.my_hash.cadena[index], value)
            return index if result != None else None  