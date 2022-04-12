n,m=map(int,input().split())

board=[]
for _ in range(n):
    row=list(input())
    board.append(row)

nbr=[]
for i in range(n-7):
    for j in range(m-7):

        res=[]
        for k in range(8):
            res.append(board[i+k][j:8+j])
        
        count=0
        for x in range(8):
            for y in range(8):
                if (x+y)%2==0:
                    if res[x][y]=='B':
                        count=count+1
                if (x+y)%2==1:
                    if res[x][y]=='W':
                        count=count+1

        if count>32:
            count=64-count
        
        nbr.append(count)

print(min(nbr))