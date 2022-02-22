string=''
n,d=map(int,input().split())
for i in range(n):
    string=string+str(i+1)
print(string.count(str(d)))