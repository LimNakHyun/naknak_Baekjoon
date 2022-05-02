from itertools import product
n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(product(sorted(a),repeat=m))
for i in b:print(i[0]) if i==1 else print(*i)