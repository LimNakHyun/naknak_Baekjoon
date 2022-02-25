result=[]
for _ in range(int(input())):
    old_name=list(map(str,input().split()))
    old_name[0]=int(old_name[0])
    result.append(old_name)
result.sort(key=lambda x:x[0])
for x in result:
    print(x[0],x[1])