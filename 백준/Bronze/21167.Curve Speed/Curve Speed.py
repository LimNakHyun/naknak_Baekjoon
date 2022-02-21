while True:
    try:
        R,S=input().split()
        print(round(((float(R)*(float(S)+.16))/.067)**(1/2)))
    except:
        break