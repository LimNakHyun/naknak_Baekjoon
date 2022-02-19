import sys
input=sys.stdin.readline

vals=[]
n=int(input().rstrip())
for i in range(n):
    x,y=map(int,input().rstrip().split())
    vals.append([y,x])
sort_vals=sorted(vals)
for i in range(len(vals)):
    for j in range(2,0,-1):
        print(sort_vals[i][j-1],end=' ')
    print('')