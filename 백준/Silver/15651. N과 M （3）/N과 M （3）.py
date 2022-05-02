from itertools import product
n,m=map(int,input().split())
a=list(product([str(i+1) for i in range(n)],repeat=m))
for i in a:print(' '.join(i))