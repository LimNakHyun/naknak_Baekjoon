vals=[]
n=int(input())
for i in range(n):
    val=list(map(int,input().split()))
    vals.append(val)
sort_vals=sorted(vals)
for i in range(len(vals)):
    for j in range(2):
        print(sort_vals[i][j],end=' ')
    print('')