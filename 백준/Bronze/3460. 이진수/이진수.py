for _ in range(int(input())):
    a=list(bin(int(input()))[2:])
    for i,j in enumerate(reversed(a)):
        if j=='1':print(i,end=' ')