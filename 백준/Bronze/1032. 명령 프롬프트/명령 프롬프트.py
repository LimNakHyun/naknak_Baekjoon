n=int(input())

word_list=[]

for _ in range(n):
    word_list.append(list(input()))

res=[]

for i in range(len(word_list[0])):
    j=0
    k=0
    while j<n-1:
        if word_list[j][i]==word_list[j+1][i]:
            k=k+1
            j=j+1
        else:
            break
    
    if k==n-1:
        res.append(word_list[0][i])
    else:
        res.append('?')

print(*res,sep='')