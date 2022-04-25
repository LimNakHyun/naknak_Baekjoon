def fibL(n):
    if(n==0):
        return 0
    i=0
    j=1
    for k in range(1,n):
        if(i>j):
            j=j+i
        else:
            i=i+j
    if(i>j):
        return i
    else:
        return j
    
fibN=int(input())
print(fibL(fibN))