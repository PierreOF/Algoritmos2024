class Node:
    def __init__(self, valor=None, prox=None):
        self.valor = valor
        self.prox = prox

    def __str__(self):
        return f"{self.valor}"

class ListaEncadeadaSimples:
    def __init__(self):
        self.ca = None  # Cabeça da lista
        self.cd = None  # Cauda da lista

    def inserirCabeca(self, valor):
        novo_node = Node(valor, self.ca)
        self.ca = novo_node
        if self.cd is None:
            self.cd = novo_node

    def inserirCauda(self, valor):
        novo_node = Node(valor, None)
        if self.cd is None:
            self.ca = novo_node
            self.cd = novo_node
        else:
            self.cd.prox = novo_node
            self.cd = novo_node

    def deletarCabeca(self):
        if self.ca is None:
            raise Exception("A lista já está vazia")
        self.ca = self.ca.prox
        if self.ca is None:
            self.cd = None

    def deletarCauda(self):
        if self.ca is None:
            raise Exception("A lista já está vazia")
        if self.ca.prox is None:
            self.ca = None
            self.cd = None
        else:
            current = self.ca
            while current.prox != self.cd:
                current = current.prox
            current.prox = None
            self.cd = current

    def __str__(self):
        valores = []
        current = self.ca
        while current is not None:
            valores.append(str(current.valor))
            current = current.prox
        return " -> ".join(valores)

    def reverse(self):
        
        anterior = None
        atual = self.ca

        while atual is not None:
            # Quem vai ser o atual na proxima iteracao
            proximo = atual.prox
            # para quem o atual vai apontar (a gente quer inverter)
            atual.prox = anterior
            anterior = atual
            atual = proximo

        self.ca , self.cd = self.cd , self.ca


# Exemplo de uso
lista = ListaEncadeadaSimples()
lista.inserirCabeca(1)
lista.inserirCauda(2)
lista.inserirCauda(3)
lista.inserirCauda(4)

print(lista)

lista.reverse()

print(lista)

