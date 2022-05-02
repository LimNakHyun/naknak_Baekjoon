from itertools import combinations
n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(combinations(sorted(a),m))
for i in b:print(i[0]) if i==1 else print(*i)