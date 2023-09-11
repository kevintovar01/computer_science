class HashColision:
    

    def lineal_colision(self, memory, index, value=None):
        aux = index

        for i in range(len(memory)):
            if value != None and value == memory[(aux+i)%len(memory)]:
                return (aux+i)%len(memory)
            elif memory[(aux+i)%len(memory)] is None and value == None:
                return (aux+i)%len(memory)
        

    def square_colision(self, memory, value, index):
        aux = index
        for i in range(len(memory)):
            if memory[(aux+(i^2))%len(memory)] is None:
                memory[(aux+(i^2))%len(memory)] = value
                break


    def doble_direccion_hash(self, memory, value, index):
        while memory[index] is not None:
            index = (((index + 1)%len(memory))+1)%len(memory)
        memory[index] = value


    def arreglo_anidado(self, memory, anidado, index, value=None):
        pass

    def lista_encadenada(self, memory, index, value=None):
        pass