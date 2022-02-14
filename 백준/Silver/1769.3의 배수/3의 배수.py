count=0
def mul3(num):
    global count
    if len(num)==1:
        return print('{}\nYES'.format(count)) if int(num)%3==0\
            else print('{}\nNO'.format(count))
    else:
        while len(num)!=1:
            num = str(sum(map(int,num)))
            count=count+1
    return mul3(num)
mul3(input())