
def fiboRecursion(int):

    if (int<=0):
        return 0
    elif (int==1):
        return 1
    else:
        return ((fiboRecursion (int - 1)) + (fiboRecursion (int - 2)))

def fiboIterative(int):

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

print (fiboRecursion(5))

print (fiboIterative(5)) 


