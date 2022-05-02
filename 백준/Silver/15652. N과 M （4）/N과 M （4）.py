from itertools import combinations_with_replacement
n,m=map(int,input().split())
a=list(combinations_with_replacement([str(i+1) for i in range(n)],m))
for i in a:print(' '.join(i))