import math
n=int(input())
sqrt=math.ceil(math.sqrt(n))
i=2
while True:
    if n%i==0:
        print(i)
        n=int(n/i)
        i=2
    else:
        i=i+1
    if i>sqrt and n!=1:
        print(n)
        break
    elif i>sqrt and n==1:
        break