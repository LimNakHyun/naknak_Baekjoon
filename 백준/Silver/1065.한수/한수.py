def digit_beegyo(N):
    m=list(str(N))
    if int(m[0])+int(m[2])==2*int(m[1]):
        return True
    else:
        return False

def hansu_count(N):
    count=0
    if N<=99:return N
    for i in range(100,N+1):
        if digit_beegyo(i)==True:
            count=count+1
    return count+99
number=int(input())
print(hansu_count(number))