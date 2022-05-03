import sys,heapq
input=sys.stdin.readline
a=[] # 힙이 담길 리스트
for _ in range(int(input())):
    b=int(input().strip()) # 숫자에 따라 힙에 넣거나 힙을 출력하거나 한다.
    heapq.heappush(a,-b) if b!=0 else print(0) if len(a)==0 else print(-heapq.heappop(a))