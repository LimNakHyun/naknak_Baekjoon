from itertools import combinations
n,m=map(int,input().split())
a=list(combinations([str(i+1) for i in range(n)],m))
for i in a:print(' '.join(i))