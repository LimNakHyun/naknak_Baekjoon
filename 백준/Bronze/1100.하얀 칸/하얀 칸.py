white=0
for i in range(1,9):
    ches=list(input())
    if i%2==1:
        for i in range(4):
            if ches[2*i]=='F':
                white=white+1
    else:
        for i in range(4):
            if ches[2*i+1]=='F':
                white=white+1
print(white)