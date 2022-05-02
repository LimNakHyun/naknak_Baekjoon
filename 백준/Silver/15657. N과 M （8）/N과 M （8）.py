from itertools import combinations_with_replacement
n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(combinations_with_replacement(sorted(a),m))
for i in b:print(i[0]) if i==1 else print(*i)