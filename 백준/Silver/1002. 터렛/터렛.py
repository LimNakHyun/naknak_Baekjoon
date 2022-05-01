n=int(input())
for i in range(n):
    x1,y1,r1,x2,y2,r2=map(int,input().split())
    if x1==x2 and y1==y2 and r1==r2:
        print(-1)
    elif x1==x2 and y1==y2 and r1!=r2:
        print(0)
    elif (x1!=x2 or y1!=y2) and (x1-x2)**2+(y1-y2)**2>(r1+r2)**2:
        print(0)
    elif (x1!=x2 or y1!=y2) and (x1-x2)**2+(y1-y2)**2==(r1+r2)**2:
        print(1)
    elif (x1!=x2 or y1!=y2) and (x1-x2)**2+(y1-y2)**2<(r1-r2)**2:
        print(0)
    elif (x1!=x2 or y1!=y2) and (x1-x2)**2+(y1-y2)**2==(r1-r2)**2:
        print(1)
    else:
        print(2)