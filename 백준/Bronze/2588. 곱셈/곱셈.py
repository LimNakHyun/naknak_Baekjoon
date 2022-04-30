a=int(input())
b=int(input())

c=list(map(int,str(b)))
c.reverse()

for i in range(len(c)):print(a*c[i])
print(a*b)