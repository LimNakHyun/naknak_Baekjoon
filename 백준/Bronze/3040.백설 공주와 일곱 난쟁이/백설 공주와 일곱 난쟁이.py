res=[]
for i in range(9):
    num=int(input())
    res.append(num)
for i in range(9):
    for j in range(1,8):
        a=res[:]
        if i==j:
            continue
        del a[i]
        del a[j-1]
        if sum(a)==100:
            for i in sorted(a):
                print(i)
            exit()