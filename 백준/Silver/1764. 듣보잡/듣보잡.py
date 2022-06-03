from collections import deque
import sys
input=sys.stdin.readline

n,m=map(int,input().strip().split())

a=deque([input().strip() for _ in range(n)])
b=set([input().strip() for _ in range(m)])

c=deque([i for i in a if i in b])

print(len(c))
print(*sorted(c),sep='\n')