for i in range(int(input())):
    alc={}
    for j in range(int(input())):
        a,b=input().split()
        alc[a]=int(b)
    print(max(alc,key=alc.get))