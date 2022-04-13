from collections import deque

n=int(input())
n_list=deque(range(1,n+1))

while len(n_list)>1:
    n_list.popleft()
    n_list.rotate(-1)

print(n_list[0])