max_num=0
index=0
for i in range(1,6):
    a=eval('+'.join(list(input().split())))
    if a>max_num:
        max_num=a
        index=i
print(index,max_num)