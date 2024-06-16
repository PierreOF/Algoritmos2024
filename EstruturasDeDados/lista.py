import numpy as np

class Node():
    def __init__(self,ant,valor,prox):
        self.prox = prox
        self.ant = ant
        self.valor = valor

    def __str__(self):
        return f"{self.valor}"

class Lista():

    def __init__(self):
        self.ca = None
        self.cd = None

    def inserirCabeca(self,valor):
        
        node = Node(None,valor,None)

        if self.ca is None:
            self.ca = node
            self.cd = node
        else:
            self.ca.ant = node
            node.prox = self.ca
            self.ca = node

    def inserirCauda(self,valor):

        node = Node(None,valor,None)

        if self.cd is None:
            self.ca = node
            self.cd = node
        else:
            node.ant = self.cd
            self.cd.prox = node
            self.cd = node

    def deletarCabeca(self):

        if self.ca.prox is None:
            raise Exception("A lista já está vazia")

        (self.ca.prox).ant = None
        self.ca = self.ca.prox
        
    def deletarCauda(self):
        
        if self.cd.ant is None:
            raise Exception("A lista já está vazia")

        self.cd = self.cd.ant


    def getLista(self):
        return f"cabeça = {self.ca} cauda = {self.cd}"



lista = Lista()

lista.inserirCabeca(10)
lista.inserirCabeca(11)
lista.inserirCabeca(12)

lista.deletarCabeca()

print(lista.getLista())
