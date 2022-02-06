alist = [0]*26
S = input() # back
for i in range(len(S)):
    for j in range(97,123):
        if ord(S[i]) == j:
            if alist[j-97] == 0:
                alist[j-97] = str(i)
            else:
                continue
for i in alist:
    if i == 0:
        print(-1,end=' ')
    else:
        print(i,end=' ')