from itertools import permutations
n,m=map(int,input().split())
a=list(permutations([str(i+1) for i in range(n)],m))
for i in a:print(' '.join(i))