import numpy as np

class Node:
    def __init__(self, ant=None, valor=None, prox=None):
        self.ant = ant
        self.valor = valor
        self.prox = prox

    def __str__(self):
        return f"{self.valor}"

class Lista:
    def __init__(self):
        self.ca = None
        self.cd = None

    def inserirCabeca(self, valor):
        node = Node(None, valor, None)

        if self.ca is None:
            self.ca = node
            self.cd = node
        else:
            self.ca.ant = node
            node.prox = self.ca
            self.ca = node

    def inserirCauda(self, valor):
        node = Node(None, valor, None)

        if self.cd is None:
            self.ca = node
            self.cd = node
        else:
            node.ant = self.cd
            self.cd.prox = node
            self.cd = node

    def deletarCabeca(self):
        if self.ca is None:
            raise Exception("A lista já está vazia")

        if self.ca.prox is None:
            self.ca = None
            self.cd = None
        else:
            self.ca = self.ca.prox
            self.ca.ant = None

    def deletarCauda(self):
        if self.cd is None:
            raise Exception("A lista já está vazia")

        if self.cd.ant is None:
            self.ca = None
            self.cd = None
        else:
            self.cd = self.cd.ant
            self.cd.prox = None


    def getLista(self):
        return f"{self.ca} {self.ca.prox} {self.cd.ant} {self.cd}"
    

lista = Lista()

lista.inserirCabeca(10)
lista.inserirCabeca(11)
lista.inserirCabeca(12)

lista.inserirCabeca(122)

print(lista.getLista())
