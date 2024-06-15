import numpy as np


# 1 

def BuscaLinear(vetor,x):
    cont = 0
    for k in vetor:

        if k == x:
            return cont
        else:
            cont += 1

    return -1

print(BuscaLinear([1,2,3,4],44 ))

# 2
#  pior caso -> Quando o elemento buscado não estiver na lista
# ==============================================================
# def BuscaLinear(vetor,x):   ->
#     cont = 0                ->   1 
#     for k in vetor:         ->   n 

#         if k == x:          ->   n
#             return cont     ->   0

#         cont += 1           ->   n

#     return -1               ->   1


# 3

def BuscaBinaria(vetor,x):

    inicio = 0
    fim = len(vetor) -1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if x == vetor[meio]:
            return meio
        elif x > vetor[meio]:
            inicio = meio + 1
        else: 
            fim = meio - 1

    return -1

vetor=[1,2,3,4,5,6,7,8,9,10]

print(BuscaBinaria(vetor,4))

# 4


# def BuscaBinaria(vetor,x):

#     inicio = 0                        -> 1
#     fim = len(vetor) -1               -> 1

#     while inicio <= fim:              -> Log(n)
#         meio = (inicio + fim) // 2    -> Log(n)

#         if x == vetor[meio]:          -> Log(n) 
#             return meio               -> 1
#         elif x > vetor[meio]:         -> 
#             inicio = meio + 1         ->
#         else:     
#             fim = meio - 1            ->

#     return -1                         -> 1



#  5 


'''
não pois está utilizando a notação
errada  
A expressão correta seria: 
“O tempo de execução de um algoritmo é pelo menos Ω"
'''

# 6
'''
não , 

array = [0,1,2,3,4,5,6,7]

MAX-HEAP 
        7
      6   5
    4  3 2  1

arrayMAX-HEAP -> [7,6,5,4,3,2,1]



'''

# 7
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

    def __str__(self):
        return str(self.fila[self.inicio:self.inicio + self.numero_elementos])
    
    
    
    
if __name__ == "__main__":
    fila = FilaCircular(10)
    
    for i in range(1,10):
        fila.enfileirar(i)

    fila.desenfileirar()
    fila.enfileirar(99)

    print(fila)
