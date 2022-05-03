from collections import deque
import sys
input=sys.stdin.readline
a=deque()
for _ in range(int(input().strip())):
    b=list(input().split())    
    a.appendleft(b[1]) if b[0]=='push_front' else a.append(b[1]) if b[0]=='push_back' else (print(-1) if not a else print(a.popleft())) if b[0]=='pop_front' else (print(-1) if not a else print(a.pop())) if b[0]=='pop_back' else print(len(a)) if b[0]=='size' else (print(1) if not a else print(0)) if b[0]=='empty' else print(-1) if not a else print(a[0]) if b[0]=='front' else (print(-1) if not a else print(a[-1]))