while True:
    sum_of_factor=0
    factors=[]
    n=int(input())
    if n==-1:
        break
    else:
        for i in range(1,n-1):
            if n%i==0:
                sum_of_factor=sum_of_factor+i
                factors.append(i)
        if sum_of_factor==n:
            print('{}'.format(n)+' = '+' + '.join(list(map(str,factors))))
        else:
            print('{} is NOT perfect.'.format(n))