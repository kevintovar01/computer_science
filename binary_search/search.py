class Search:
    def __init__(self, length) -> None:
        self.memory = []
        self.length = length


    def append_list(self, value):
        if value in self.memory:
            return f"Clave {value} ya se encuentra en la estructura"
        
        if len(self.memory) < self.length:
            self.memory.append(value)
            return f"Clave {value} insertada en la posicion {0}"
        else:
            return f"Espacio insuficiente De la Estructura"
        

    def delete(self, value):        
        try:
            self.memory.remove(value)
            return f"La clave {value} ha sido eliminada de la estructura"
        except:
            return f"La clave {value} No se encuentra en la estructura"

    def binary_search(self, objective):

        left = 0
        right = len(self.memory)-1

        while left <= right:

            medio = (left+right)//2
            if self.memory[medio] == objective:
                return f"La clave {objective} se encuentra en la posicion"
            elif self.memory[medio] < objective:
                left = medio+1
            else:
                right = medio-1
    
        return f"La clave {objective} No se encuentra en la estructura"
    

    def sequence_search(self, objective):
        for i,value in self.memory:
            if value == objective:
                return f"La clave {objective} se encuentra en la posicion {i}"
        return f"La clave {objective} No se encuentra en la estructura"
    

    def bubble_sort(self):
        len_list = len(self.memory)
        aux_list = self.memory

        for i in range(len_list):
            for j in range(len_list-i-1): #this decrements the list, for don't repeat iterations to future
                if self.memory[j] > self.memory[j+1]:
                    self.memory[j], self.memory[j+1] = self.memory[j+1], self.memory[j]

        return f" La estructura ha sido ordenada"