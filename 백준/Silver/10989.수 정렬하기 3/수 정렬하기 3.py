import sys
input=sys.stdin.readline
b=[0]*10001
n=int(input().rstrip())
for i in range(n):
    a=int(input().rstrip())
    b[a]=b[a]+1
for i,num in enumerate(b):
    if num!=0:
        for j in range(num):
            print(i)