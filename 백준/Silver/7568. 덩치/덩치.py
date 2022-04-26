info=[]
n=int(input())

for _ in range(n):
    info.append(list(map(int,input().split())))

res=[]
for i in range(n):
    count=0
    for j in range(n):
        temp=0
        for k in range(2):
            if i==j:
                pass
            else:
                if info[j][k]>info[i][k]:
                    temp=temp+1
        if temp==2:
            count=count+1
    res.append(count+1)

print(*res, sep=' ')