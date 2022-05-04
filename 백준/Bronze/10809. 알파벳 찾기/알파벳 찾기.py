a=[-1]*26
s=list(input())
for i,j in enumerate(s):
    if a[ord(j)-97]==-1:a[ord(j)-97]=i
print(*a)