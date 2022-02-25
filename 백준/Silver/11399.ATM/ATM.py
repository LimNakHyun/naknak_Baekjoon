n=int(input())
num_list=list(map(int,input().split()))
num_list.sort()

res=0
for i in range(n):
    middle_num=0
    for j in range(i+1):
        middle_num=middle_num+num_list[j]
    res=res+middle_num
print(res)