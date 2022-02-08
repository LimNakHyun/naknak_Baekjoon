min_num=100
odd_sum=0
for i in range(7):
    num=int(input())
    if num%2==1:
        odd_sum=odd_sum+num
        if num<min_num:
            min_num=num
        else:
            pass
    else:
        pass

if odd_sum!=0:
    print(odd_sum)
    print(min_num)
else:
    print(-1)