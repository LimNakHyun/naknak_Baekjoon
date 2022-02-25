def gcd(m,n):
    if  n>m:
        m,n=n,m
    if m%n==0:
        return n
    return gcd(n,m%n)

n=int(input())
for i in range(n):
    sum_gcd=0
    num=list(map(int,input().split()))
    for i in range(1,num[0]+1):
        for j in range(i+1,num[0]+1):
            sum_gcd=sum_gcd+gcd(num[i],num[j])
    print(sum_gcd)