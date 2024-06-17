
import numpy as np

class FilaCircular:
    def __init__(self, capacidade) -> None:
        self.capacidade = capacidade
        self.inicio = 0
        self.fim = -1
        self.numero_elementos = 0
        self.fila = np.empty(capacidade, dtype=int)
        
    def enfileirar(self, valor):
        if self.numero_elementos == self.capacidade:
            print("A fila já está cheia")
            return
    
        if self.fim == self.capacidade - 1:
            self.fim = -1
        self.fim += 1
        self.fila[self.fim] = valor
        self.numero_elementos += 1
        
    def desenfileirar(self):
        if self.numero_elementos == 0:
            print("A fila está vazia")
            return
        temp = self.fila[self.inicio]
        self.inicio += 1
        if self.inicio == self.capacidade - 1:
            self.inicio = 0
        self.numero_elementos -= 1
        return temp
    
    
    
    
if __name__ == "__main__":
    fila = FilaCircular(3)
    fila.enfileirar(1)
    fila.enfileirar(2)
    fila.enfileirar(3)
    fila.desenfileirar()
    fila.enfileirar(1)
