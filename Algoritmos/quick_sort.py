import numpy as np

def quicksort(vetor):

    if len(vetor) <= 1:                                                    # -> O(1) 
        return vetor
    else:
        pivo = vetor[len(vetor)//2]                                        # -> O(1)

        left = [x for x in vetor if x < pivo ]                             # -> O(n) 
        middle = [x for x in vetor if x == pivo ]                          # -> O(n)
        right = [x for x in vetor if x > pivo ]                            # -> O(n)

        return (quicksort(left) + middle + quicksort(right))              #  -> T(n) = 2T(n/2) + O(n)

# T(n/2): Tempo para ordenar as sublistas left e right.

# O(n): Tempo para dividir a lista original em sublistas e concatenar as sublistas ordenadas.

arrei = np.array([1,2,5,6,8,2,4,6])

print(quicksort(arrei))



