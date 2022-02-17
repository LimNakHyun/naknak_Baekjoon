while True:
    try:
        n=int(input())
        for i in range(1,10000):
            m='1'*i
            if int(m)%n==0:
                print(i)
                break
    except:
        break