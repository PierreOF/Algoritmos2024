import numpy as np

#  Complexidade = O(n.n) para o pior caso

def insertion_sort(arr):

    for i in range(1 , len(arr)):       # -> O(n-1) pois começa apartir do 2 elemento do array

        key = arr[i]                    # -> O(1)
        j = i - 1                       # -> O(1)

        while j >= 0 and key < arr[j]:  # -> O(n) para o pior caso
            
            arr[j+1] = arr[j]           # -> O(1)
            
            j-=1                        # -> O(1)

        arr[j+1] = key                  # -> O(1)

# T(n) = T(n-1) + O(n)  -> FORMA RECURSIVA

