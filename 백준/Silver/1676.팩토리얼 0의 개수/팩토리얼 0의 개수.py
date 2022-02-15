n=int(input())
num=0
for i in range(1,(n//5)+1):
    a=list(map(lambda x : x%(5**i)==0, range(1,n+1)))
    num=num+sum(a)
print(num)