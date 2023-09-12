from binary_search import binary_search 


class HashColision:

    def __init__(self, my_hash) -> None:
        self.my_hash = my_hash
        self.lenght = self.my_hash.lenght
    

    def lineal_colision(self, memory, index, value=None):
        aux = index

        for i in range(self.lenght):
            if value != None and value == memory[(aux+i)%self.lenght]:
                return (aux+i)%self.lenght
            elif memory[(aux+i)%self.lenght] is None and value == None:
                return (aux+i)%self.lenght

        

    def square_colision(self, memory, index, value=None):
        aux = index
        for i in range(self.lenght):
            if value != None and value == memory[(aux+(i^2))%self.lenght]:
                return (aux+(i**2))%self.lenght
            elif memory[(aux+(i**2))%self.lenght] is None and value == None:
                return (aux+(i**2))%self.lenght


    def doble_direccion_hash(self, memory, index, value=None):
        while value != None:
            index = (((index + 1)%self.lenght)+1)%self.lenght
            if value ==  memory[index]:
                return index

        while memory[index] is not None:
            index = (((index + 1)%self.lenght)+1)%self.lenght
        return index


    def arreglo_anidado(self, memory, index, value=None):
        for i in range (len(memory)-1):
          if self.my_hash.anidado[index][i] is not None:
            self.my_hash.anidado[index][i]=value
            break

    def lista_encadenada(self, memory, index, value=None):
        if value == None:
            self.my_hash.cadena[index].append(self.my_hash.key)
        else:
            result = binary_search(self.my_hash.cadena[index], value)
            return index if result != -1 else None


                
        
        
        