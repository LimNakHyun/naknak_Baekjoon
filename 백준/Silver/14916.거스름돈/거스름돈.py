n=int(input())
res=[]
for i in range((n//5)+1):
    if (n-(i*5))%2==0:
        res.append(i+(n-(i*5))//2)
if len(res)==0:
    print(-1)
else:
    print(min(res))