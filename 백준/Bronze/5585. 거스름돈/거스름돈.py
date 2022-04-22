n=int(input())
n=1000-n
count=0
while n!=0:
    if n>=500:
        count=count+1
        n=n-500
    elif n>=100 and n<500:
        count=count+(n//100)
        n=n-100*(n//100)
    elif n>=50 and n<100:
        count=count+1
        n=n-50
    elif n>=10 and n<50:
        count=count+(n//10)
        n=n-10*(n//10)
    elif n>=5 and n<10:
        count=count+(n//5)
        n=n-5*(n//5)
    else:
        count=count+n
        n=0

print(count)