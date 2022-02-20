num_list=[int(input()) for i in range(10)]

def list_sum(slis,num):
    return sum(slis[:num])

for i in range(1,11):
    ans=list_sum(num_list,i)
    if ans==100:
        print(ans)
        exit()
    elif i==10 and ans<100:
        print(ans)
    elif ans>100:
        if ans-100>100-list_sum(num_list,i-1):
            print(list_sum(num_list,i-1))
        else:
            print(ans)
        exit()