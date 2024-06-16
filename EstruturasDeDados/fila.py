import numpy as np


class Fila():

    def __init__(self,length):
        self.cd = 0
        self.ca = 0
        self.length = length
        self.vetor = np.empty(length,dtype=int)

    def enqueue(self,valor):

        if self.cd == self.length:
            raise Exception("Lista cheia")
        
        self.vetor[self.cd] = valor
        self.cd += 1

    def deqeue(self):

        if self.cd == self.ca:
            raise Exception("UnderFlow")
        

        self.ca += 1

    def __str__(self):
        if self.ca == self.cd:
            return "Fila vazia"
        return " -> ".join(map(str, self.vetor[self.ca:self.cd]))


fila = Fila(3)

fila.enqueue(1)
fila.enqueue(4)
fila.enqueue(3)
fila.deqeue()
fila.enqueue(40)


print(fila.__str__())