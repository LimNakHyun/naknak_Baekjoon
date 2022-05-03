import sys,heapq
input=sys.stdin.readline
q=[]
for i in range(int(input().strip())):
    a=int(input().strip())
    heapq.heappush(q,(abs(a),a)) if a!=0 else print(a) if not q else print(heapq.heappop(q)[1])