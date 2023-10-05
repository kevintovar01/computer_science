class Est_Parcial:
    
    def __init__(self, cubetas, filas, tasa_expansion, tasa_reduccion):
        self.cubetas = cubetas
        self.filas = filas
        self.tasa_expansion = tasa_expansion
        self.tasa_reduccion = tasa_reduccion
        self.memoria = [[0 for _ in range(cubetas)] for _ in range(filas)]
        self.lista_colisiones = [0 for _ in range(filas * cubetas)]
        self.historial_claves = []
        self.claves_totales = 0
        self.aux_cubetas = False

    def agregar_clave(self, indice, clave):
        
        for clave_guardada in self.historial_claves:
            if clave_guardada == clave:
                print("La clave ya se encuentra en la memoria")
                return True
        self.historial_claves.append(clave)
        
        aux = False
        for i in range(self.filas):
            if self.memoria[i][indice] == 0:
                self.memoria[i][indice] = clave
                aux = True
                print(f"La clave {clave} se ha insertado en la cubeta {indice} en la fila {i} satisfactoriamente.")
                break
        if not aux:
            for i in range(self.filas * self.cubetas):
                if self.lista_colisiones[i] == 0:
                    self.lista_colisiones[i] = clave
                    print(f"Se presentó una colisión en la cubeta {indice}, por lo cual la clave {clave} será insertada en la lista de colisiones.")
                    break

        self.claves_totales += 1

        if (self.claves_totales / (self.filas * self.cubetas)) > self.tasa_expansion:
            self.expandir()
            return False

        return True

    def expandir(self):
        
        if not self.aux_cubetas:
            aux = self.cubetas // 2
            self.aux_cubetas = True
        else:
            aux = int(self.cubetas * 0.333)
            self.aux_cubetas = False

        self.cubetas += aux
        print(f"La tasa de Expansión ha sido superada, por lo que vamos a expandir la estructura.\nEl nuevo número de cubetas será {self.cubetas}")
        self.memoria = [[0 for _ in range(self.cubetas)] for _ in range(self.filas)]
        self.lista_colisiones = [0 for _ in range(self.filas * self.cubetas)]
        self.historial_claves = []
        self.claves_totales = 0

    def eliminar_clave(self, indice, clave):
        
        self.historial_claves.remove(clave)
        
        aux = False
        for i in range(self.filas):
            if self.memoria[i][indice] == clave:
                self.memoria[i][indice] = 0
                aux = True
                self.claves_totales -= 1
                print(f"La clave {clave} que se ha encontrado en la cubeta {indice} ha sido eliminada correctamente.")
                break

        if not aux:
            aux2 = False
            for i in range(self.filas * self.cubetas):
                if self.lista_colisiones[i] == clave:
                    self.lista_colisiones[i] = 0
                    aux2 = True
                    self.claves_totales -= 1
                    print(f"La clave {clave} que se ha encontrado en la lista de colisiones ha sido eliminada correctamente.")
                    break

            if not aux2:
                print("La clave no se encuentra en el arreglo.")

        if (self.claves_totales / self.cubetas) < self.tasa_reduccion:
            self.reducir()
            return False

        return True

    def reducir(self):
        
        if not self.aux_cubetas:
            aux = self.cubetas // 4
            self.aux_cubetas = True
        else:
            aux = self.cubetas // 3
            self.aux_cubetas = False

        self.cubetas -= aux
        print(f"La tasa de Reducción ha sido superada, por lo que vamos a reducir la estructura.\nEl nuevo número de cubetas será {self.cubetas}")
        self.memoria = [[0 for _ in range(self.cubetas)] for _ in range(self.filas)]
        self.lista_colisiones = [0 for _ in range(self.filas * self.cubetas)]

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
        colisiones = "[" + ", ".join(str(self.lista_colisiones[i]) for i in range(self.filas * self.cubetas)) + "]"
        print(colisiones)
