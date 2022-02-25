def digit_sum(nbr):
    str_nbr=str(nbr)
    return nbr+eval('+'.join(str_nbr))

num_list=list(range(1,10000))
result=set(map(digit_sum,num_list))
# print(result)

final_list=[str(i) for i in num_list if i not in result]

print(' '.join(final_list))