


# 1 O(n)

# 2

def fatorial(int):


    if (int == 0) or (int == 1):
        return 1 
    elif int > 1:
        return int * fatorial(int-1)
    
#  T(n) = T(n) + O(1)

# 3 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def reverse(self):
        prev = None
        current = self.head
        self.tail = self.head  # A nova cauda será a cabeça antiga
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev


ll = LinkedList()

ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

ll.reverse()



# 4 
    
'''
O problema de uso excessivo de memória pelo compilador, 
ao compilar o trecho de código, é provavelmente causado 
pela profundidade da recursão. 
A pilha de execução do compilador está se enchendo devido
às muitas chamadas recursivas, levando a um estouro de memória.
A substituição de recursão por iteração pode resolver
esse problema, evitando o uso excessivo de memória e 
melhorando a eficiência do código.
'''





