def dice(yoot):
    nz=yoot.count(0)

    if nz==0:return 'E'
    elif nz==1:return 'A'
    elif nz==2:return 'B'
    elif nz==3:return 'C'
    else:return 'D'

for _ in range(3):
    yoot=list(map(int,input().split()))
    print(dice(yoot))