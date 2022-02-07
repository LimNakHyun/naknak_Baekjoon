n,m=map(int,input().split())
a=list(map(int,input().split()))
min_sum=0
for i in range(len(a)):
    for j in range(1,len(a)):
        for k in range(2,len(a)):
            if i==j or j==k or k==i:
                continue
            if a[i]+a[j]+a[k]<=m and min_sum<=a[i]+a[j]+a[k]:
                min_sum=a[i]+a[j]+a[k]
print(min_sum)