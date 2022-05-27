from collections import deque
import sys
input=sys.stdin.readline

for _ in range(int(input())):

    funcs=list(input().strip())

    n=int(input())
    m=input().strip()[1:-1].split(',')
    dq=deque(m)
    if n==0:dq=[]
    
    rev=0
    dcount=funcs.count('D')

    for func in funcs:
        if len(dq)==0:
            break
        elif func=='R':
            rev=rev+1
        else:
            dq.popleft() if rev%2==0 else dq.pop()

    if rev%2!=0:dq.reverse()

    print('['+','.join(list(dq))+']') if n>=dcount else print('error')