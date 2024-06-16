import numpy as np

class Pilha:

    def __init__(self,length):
        self.top = 0
        self.length = length
        self.vetor = np.empty(length,dtype=int) 

    def push(self,valor):

        if self.top == self.length:
            raise Exception("OverFlow")

        self.vetor[self.top] = valor
        self.top += 1 

    def pop(self):

        if self.top == 0:
            raise Exception("UnderFlow")
        
        self.top -= 1

    def getArray(self):
        return self.vetor
