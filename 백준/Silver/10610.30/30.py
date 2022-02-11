n=list(input())
sum_n=sum([int(i) for i in n])
if sum_n%3!=0:
    print(-1)
elif [int(i) for i in n].count(0)==0:
    print(-1)
else:
    result=[int(i) for i in n]
    f_res=reversed(sorted(result))
    print(''.join(str(i) for i in f_res))