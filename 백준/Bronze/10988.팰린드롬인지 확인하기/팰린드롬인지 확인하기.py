n_list=list(input())
nbool='1'
if len(n_list)==1:
    nbool='1'
else:
    for i in range((len(n_list)//2)):
        if n_list[i]!=n_list[len(n_list)-1-i]:
            nbool='0'
            break
print(nbool)