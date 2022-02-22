n=int(input())
sqmat=[]
check_list=[]
for i in range(n):
    line=list(map(int,input().split()))
    sqmat.append(line)
    check_list=check_list+line
if len(set(check_list))!=n*n:
    print('FALSE')
    exit()

falsecnt=0

for i in range(n):
    if sum(sqmat[i])!=int(n*((n*n)+1)/2):
        falsecnt=falsecnt+1

for i in range(n):
    linesum=0
    for j in range(n):
        linesum=linesum+sqmat[i][j]
    if linesum!=int(n*((n*n)+1)/2):
        falsecnt=falsecnt+1

diagsum1=0
for i in range(n):
    diagsum1=diagsum1+sqmat[i][i]
if diagsum1!=int(n*((n*n)+1)/2):
    falsecnt=falsecnt+1

diagsum2=0
for i in range(n):
    diagsum2=diagsum2+sqmat[i][n-1-i]
if diagsum2!=int(n*((n*n)+1)/2):
    falsecnt=falsecnt+1

if falsecnt==0:
    print('TRUE')
else:
    print('FALSE')