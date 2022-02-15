def sp(n):
    if n==1:return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

x=int(input())
y=int(input())
sum=0
smallest_prime=0
for i in range(y,x-1,-1):
    if sp(i)==True:
        sum=sum+i
        smallest_prime=i
if smallest_prime==0:
    print(-1)
else:
    print(sum)
    print(smallest_prime)