ft=[500,300,200,50,30,10]
st=[512,256,128,64,32]

for i in range(int(input())):
    
    fr=0
    sr=0

    a,b=map(int,input().split())
    if a==1:
        fr=ft[0]
    elif a==2 or a==3:
        fr=ft[1]
    elif a>=4 and a<=6:
        fr=ft[2]
    elif a>=7 and a<=10:
        fr=ft[3]
    elif a>=11 and a<=15:
        fr=ft[4]
    elif a>=16 and a<=21:
        fr=ft[5]
    else:
        fr=0

    if b==1:
        sr=st[0]
    elif b==2 or b==3:
        sr=st[1]
    elif b>=4 and b<=7:
        sr=st[2]
    elif b>=8 and b<=15:
        sr=st[3]
    elif b>=16 and b<=31:
        sr=st[4]
    else:
        sr=0
        
    print((fr+sr)*10000)