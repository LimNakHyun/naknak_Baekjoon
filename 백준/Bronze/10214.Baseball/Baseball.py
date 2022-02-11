n=int(input())
for i in range(n):
    yonsei=0
    korea=0
    for j in range(9):
        a,b=map(int,input().split())
        yonsei=yonsei+a
        korea=korea+b
    if yonsei>korea:
        print('Yonsei')
    elif yonsei<korea:
        print('Korea')
    else:
        print('Draw')