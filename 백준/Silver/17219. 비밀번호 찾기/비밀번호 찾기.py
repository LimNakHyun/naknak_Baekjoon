import sys
input=sys.stdin.readline

n,m=map(int,input().strip().split())
accounts={}

for _ in range(n):
    id,pw=input().strip().split()
    accounts[id]=pw

for _ in range(m):
    id=input().strip()
    print(accounts[id])