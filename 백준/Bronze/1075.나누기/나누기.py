n=input()
f=int(input())
for i in range(10):
    for j in range(10):
        n=n[:-2]+str(i)+str(j)
        if int(n)%f==0:
            print(str(i)+str(j))
            exit()