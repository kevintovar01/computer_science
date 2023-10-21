from function_hash.binary_search import binary_search 

class Est_Parcial:
    
    def __init__(self, cubetas, filas, tasa_expansion, tasa_reduccion, tipo_expansion):
        self.cubetas = cubetas       
        self.filas = filas
        self.tasa_expansion = tasa_expansion
        self.tasa_reduccion = tasa_reduccion
        self.memoria = [[0 for _ in range(cubetas)] for _ in range(filas)]
        self.lista_colisiones =  {i:[] for i in range(cubetas)}
        self.historial_claves = []
        self.claves_totales = 0
        self.initial_length = self.cubetas
        self.function_hash = None
        self.my_hash = None
        self.tipo_expansion = tipo_expansion


    def buscar_clave(self, clave):
        # Primero, buscamos en la memoria principal.
        for indice in range(self.cubetas):
            for fila in range(self.filas):
                if self.memoria[fila][indice] == clave:
                    return {"tipo": "Memoria Principal", "indice": indice, "fila": fila}
        
        # Si no está en la memoria principal, buscamos en la lista de colisiones.
        for posicion in range(self.cubetas):
            if binary_search(self.lista_colisiones[posicion], clave) != None:
                return {"tipo": "Lista de Colisiones", "posicion": posicion}


        # Si no se encuentra en ninguno de los dos lugares, retornamos None.
        return False   

    def agregar_clave(self, indice, clave):
        if clave in self.historial_claves:
            return True, "La clave ya se encuentra en la memoria"
        self.historial_claves.append(clave)

        # while indice > len(self.memoria)-1:
        #     indice -= 1
        
        aux = False
        for i in range(self.filas):
            if self.memoria[i][indice] == 0:
                self.memoria[i][indice] = clave
                aux = True
                message = f"La clave {clave} se ha insertado en la cubeta {indice} en la fila {i} satisfactoriamente."
                break

        if not aux:
            self.lista_colisiones[indice].append(clave)
            message = f"Se presentó una colisión en la cubeta {indice}, por lo cual la clave {clave} será insertada en la lista de colisiones."
            

        self.claves_totales += 1

        if (self.claves_totales / (self.filas * self.cubetas)) > self.tasa_expansion/100:
            message += self.expandir()
            return False, message

        return True, message


    def expandir(self):
        if self.tipo_expansion == "total":
            self.cubetas = self.cubetas * 2
            self.memoria = [[0 for _ in range(self.cubetas)] for _ in range(self.filas)]
        else:
            if self.cubetas > 3:
                aux = self.cubetas
                self.memoria = [[0 for _ in range(self.previous*2)] for _ in range(self.filas)]
                self.cubetas = self.previous*2
                self.previous = aux
            else:
                self.previous = self.cubetas
                self.cubetas+=1
                self.memoria = [[0 for _ in range(self.cubetas)] for _ in range(self.filas)]


        message = f", La tasa de Expansión ha sido superada, por lo que vamos a expandir la estructura.\nEl nuevo número de cubetas será {self.cubetas}"
        self.lista_colisiones = {i:[] for i in range(self.cubetas)}
        aux = self.historial_claves
        self.historial_claves = []
        self.claves_totales = 0

        for i in aux:
            self.my_hash.length = self.cubetas
            self.my_hash.prime = self.cubetas
            index = self.function_hash(i)-1
            self.agregar_clave(index,i)

        return message



    def eliminar_clave(self, clave):
        # Usar el método de búsqueda
        resultado = self.buscar_clave(clave)
        
        # Si no encontramos la clave
        if resultado == False:
            return False, f"La clave no se encuentra en la estructura."
        
        # Si la clave está en la memoria principal
        if resultado["tipo"] == "Memoria Principal":
            self.memoria[resultado['fila']][resultado['indice']] = 0
            if len(self.lista_colisiones[resultado['indice']]) > 0:
                self.memoria[resultado['fila']][resultado['indice']] = self.lista_colisiones[resultado['indice']][0]
                self.lista_colisiones[resultado['indice']].pop(0)
            message = f"La clave {clave} que se ha encontrado en la cubeta {resultado['indice']} ha sido eliminada correctamente."
            
        # Si la clave está en la lista de colisiones
        elif resultado["tipo"] == "Lista de Colisiones":
            self.lista_colisiones[resultado['posicion']].remove(clave)
            message= f"La clave {clave} que se ha encontrado en la lista de colisiones ha sido eliminada correctamente."
        
        # Actualizar el historial de claves y el total
        self.historial_claves.remove(clave)
        self.claves_totales -= 1
        
        # Revisar si necesitamos reducir
        if (self.claves_totales / self.cubetas) < self.tasa_reduccion/100 and self.cubetas != 2:
            message += self.reducir()
            return False, message

        return True, message


    def reducir(self):    
        if self.tipo_expansion == "total":
            self.cubetas = int(self.cubetas / 2)
        else:
            aux = self.previous
            self.previous = int(self.cubetas/2)
            self.cubetas = aux

        
        message = f", La tasa de Reducción ha sido superada, por lo que vamos a reducir la estructura.\nEl nuevo número de cubetas será {self.cubetas}"
        self.memoria = [[0 for _ in range(self.cubetas)] for _ in range(self.filas)]
        self.lista_colisiones =  {i:[] for i in range(self.cubetas)}

        aux = self.historial_claves
        self.historial_claves = []
        self.claves_totales = 0

        for i in aux:
            self.my_hash.length = self.cubetas
            self.my_hash.prime = self.cubetas
            index = self.function_hash(i)-1
            self.agregar_clave(index,i)

        return message


    def get_cubetas(self):
        return self.cubetas


    def get_historial_claves(self):
        return self.historial_claves
        

    def imprimir_estructura(self):
        
        print("Memoria Principal:")
        for i in range(self.filas):
            row = "[" + ", ".join(str(self.memoria[i][j]) for j in range(self.cubetas)) + "]"
            print(row)

        print("Lista de Colisiones: ")

        colisiones = "[" + ", ".join(str(self.lista_colisiones[i]) for i in range(self.cubetas)) + "]"
        print(colisiones)


    def print_all(self):
        print(self.tipo_expansion)
        self.imprimir_estructura()
        print("Historial de claves")
        self.historial_claves
        print(f"tasa de expansion {self.tasa_expansion}%")
        print(f"tasa de reduccion {self.tasa_reduccion}%")
        print(f"Cuebetas: {self.cubetas}")




    def reset_list(self):
        self.__init__(self.initial_length, self.filas, self.tasa_expansion, self.tasa_reduccion, self.tipo_expansion)
