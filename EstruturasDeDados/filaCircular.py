import numpy as np


class FilaCircular():

    def __init__(self,length):
        self.elementos = 0
        self.inicio = 0
        self.fim = -1
        self.length = length
        self.array = np.empty(length,dtype=int)

    def __str__(self):

        return f'inicio:{self.inicio}  fim:{self.fim}'

    def enfileirar(self,valor):
        
        if self.elementos == self.length:
            raise Exception("Lista cheia já")
        
        if self.fim == self.length-1:
            self.fim = -1

        self.fim += 1
        self.array[self.fim] = valor
        self.elementos += 1

    def desenfileirar(self):

        if self.elementos == 0:
            raise Exception("Lista vazia")
        
        self.inicio += 1

        if self.inicio == self.length-1:
            self.inicio = 0

        self.elementos -= 1
        


fila = FilaCircular(10)

for i in range(1,11):
    fila.enfileirar(i)

fila.desenfileirar()
fila.enfileirar(55)

print(fila)





