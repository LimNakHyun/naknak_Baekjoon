n,k=map(int,input().split())
num=list(range(2,n+1))
count=0
for i in range(2,1001):
    for j in range(len(num)):
        if num[j]%i==0:
            count=count+1
            if count==k:
                print(num[j])
                exit()
            else:
                num[j]=1217