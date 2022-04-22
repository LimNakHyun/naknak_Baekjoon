from collections import deque
n,k=map(int,input().split())
queue=deque([i+1 for i in range(n)])
res=[]

while queue:
    for _ in range(k-1):
        queue.append(queue.popleft())
    res.append(queue.popleft())

res=[str(i) for i in res]
print('<'+', '.join(res)+'>')