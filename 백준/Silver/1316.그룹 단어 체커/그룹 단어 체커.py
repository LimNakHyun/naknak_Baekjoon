n=int(input())
count=0
for j in range(n):
    s=input()
    res=[s[0]]
    for i in range(1,len(s)):
        if s[i]!=s[i-1]:
            res.append(s[i])
    if len(res)==len(set(res)):
        count=count+1
print(count)