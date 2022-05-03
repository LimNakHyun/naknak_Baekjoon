from collections import deque
n,k=map(int,input().split())
a=deque([i+1 for i in range(n)])
res=[]
while a:
    for _ in range(k-1):a.append(a.popleft())
    res.append(str(a.popleft()))
print('<'+', '.join(res)+'>')