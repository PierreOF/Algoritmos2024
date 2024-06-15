
def fibonnaci(int):

    if (int<=0):
        return 0
    elif (int==1):
        return 1
    else:
        return ((fibonnaci (int - 1)) + (fibonnaci (int - 2)))

def fibo(int):

    if (int <= 0):
        return 0
    elif (int == 1):
        return 1
    else:
        t1 = 0
        t2 = 1
        
        for x in range(1,int):
            t3 = t1 + t2
            
            t1 = t2
            t2 = t3
        
        return t3



#  0 1 1 2 3 5 8 13 21 34 55 

print (fibonnaci(5))

print (fibo(5)) 


