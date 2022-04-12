n=int(input())
nsum=0
for i in range(n+2):
    nsum=nsum+i
    if nsum>n:
        print(i-1)
        exit()