import sys,heapq
input=sys.stdin.readline
a=[]
for _ in range(int(input().strip())):
    b=int(input().strip())
    heapq.heappush(a,b) if b!=0 else print(0) if len(a)==0 else print(heapq.heappop(a))