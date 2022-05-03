n=int(input().strip())
a=list(map(int,input().strip().split()))
a.sort()
print(a[len(a)//2]**2) if len(a)%2==1 else print(a[0]*a[-1])