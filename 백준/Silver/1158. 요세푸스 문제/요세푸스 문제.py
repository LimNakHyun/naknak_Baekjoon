from collections import deque
n,k=map(int,input().split())
a=deque([i+1 for i in range(n)])
res=[]
while a:
    a.rotate(-k+1)
    res.append(str(a.popleft()))
print('<'+', '.join(res)+'>')