import sys
input=sys.stdin.readline

h,x=map(int,input().rstrip().split())
sm=0
c=1
for i in range(h):
    c=c*x
    c=c%1000000007
    sm=sm+int(input().rstrip())*c
    sm=sm%1000000007
print(sm)