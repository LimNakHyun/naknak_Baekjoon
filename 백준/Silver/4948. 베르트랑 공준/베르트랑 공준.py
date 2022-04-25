import math

def prime_count(a,b):
    boolean_list=[True]*(b+1)

    for i in range(2,int(math.sqrt(b)+1)):
        if boolean_list[i]==True:
            for j in range(i*2,b+1,i):
                boolean_list[j]=False
    
    boolean_list=boolean_list[a+1:b+2]
    return sum(boolean_list)

while True:
    n=int(input())
    if n==0:
        break
    print(prime_count(n,2*n))