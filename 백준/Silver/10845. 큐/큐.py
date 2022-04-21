from collections import deque
import sys
input=sys.stdin.readline

n=int(input())
m=deque([])

for _ in range(n):
    ope=input().strip().split()

    if ope[0]=='push':
        m.append(ope[1])
    
    if ope[0]=='pop':
        if len(m)==0:
            print(-1)
        else:
            print(m.popleft())
    
    if ope[0]=='size':
        print(len(m))
    
    if ope[0]=='empty':
        if len(m)==0:
            print(1)
        else:
            print(0)
    
    if ope[0]=='front':
        if len(m)==0:
            print(-1)
        else:
            print(m[0])
    
    if ope[0]=='back':
        if len(m)==0:
            print(-1)
        else:
            print(m[len(m)-1])