for _ in range(int(input())):
    a,b=input().split()
    print(str(bin(int(a,2)+int(b,2)))[2:])