n=int(input())
for i in range(n):
    def gcd(m,n):
        if  n>m:
            m,n=n,m
        if m%n==0:
            return n
        return gcd(n,m%n)
    
    a,b=map(int,input().split())
    gcd=gcd(a,b)
    print(int((a*b)/gcd))