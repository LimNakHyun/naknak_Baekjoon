from collections import deque
import sys
input=sys.stdin.readline

n=int(input().strip())
m=deque([])

for _ in range(n):
    ope=list(input().strip().replace('_',' ').split())

    if ope[0]=='push':
        if ope[1]=='front':
            m.appendleft(ope[2])
        if ope[1]=='back':
            m.append(ope[2])
    
    if ope[0]=='pop':
        if ope[1]=='front':
            if len(m)==0:
                print(-1)
            else:
                print(m.popleft())
        if ope[1]=='back':
            if len(m)==0:
                print(-1)
            else:
                print(m.pop())

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
            print(m[-1])