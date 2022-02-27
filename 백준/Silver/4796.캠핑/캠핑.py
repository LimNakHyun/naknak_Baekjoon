i=0
while True:
    l,p,v=map(int,input().split())
    if l==0 and p==0 and v==0:
        exit()
    i=i+1
    quotient=v//p
    remainder=v%p
    result=0
    
    if remainder>l:
        result=l*quotient+l
    else:
        result=l*quotient+remainder    
    
    print('Case {}: {}'.format(i,result))