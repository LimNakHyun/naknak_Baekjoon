import sys
input=sys.stdin.readline

a=[list(input().strip().split()) for _ in range(int(input()))]
for ls in a:
    for i in range(1,4):ls[i]=int(ls[i])
a.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))
for ls in a:print(ls[0])