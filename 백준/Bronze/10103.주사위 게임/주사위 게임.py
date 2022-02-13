cha=100
san=100
for i in range(int(input())):
    a,b=map(int,input().split())
    if a>b:
        san=san-a
    elif a<b:
        cha=cha-b
print('{}\n{}'.format(cha,san))