n,k=map(int,input().split())
res=[]

for i in range(n):
    res.append(int(input()))

count=0
for i in range(n):
    if res[n-i-1]<=k:
        quotient=k//res[n-i-1]
        k=k%res[n-i-1]
        count=count+quotient
print(count)