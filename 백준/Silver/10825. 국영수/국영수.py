a=[]
for _ in range(int(input())):
    a.append(input().split())

for ls in a:
    ls[1]=int(ls[1])
    ls[2]=int(ls[2])
    ls[3]=int(ls[3])

a.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))

for ls in a:
    print(ls[0])