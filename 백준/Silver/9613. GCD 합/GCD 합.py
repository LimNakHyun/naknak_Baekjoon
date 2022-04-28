def gcd(m,n):
    if  n>m:m,n=n,m
    if m%n==0:return n
    return gcd(n,m%n)

for _ in range(int(input())):
    _sum=0
    m,*arr=map(int,input().split())
    for j in range(m):
        for k in range(j+1,m):
            _sum=_sum+gcd(arr[j],arr[k])
    print(_sum)