result=[0 for x in range(int(input()))]

list_a=list(map(int,input().split()))
list_b=list(map(int,input().split()))

list_a.sort()
list_b.sort(reverse=True)

res=0
for i in range(len(result)):
    res=res+list_a[i]*list_b[i]
print(res)