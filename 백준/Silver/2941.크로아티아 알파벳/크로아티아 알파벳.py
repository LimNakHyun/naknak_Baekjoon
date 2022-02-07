s=input()
count=0
for i in range(len(s)):
    if s[i]=='=' or s[i]=='-':
        if s[i-1]=='z' and s[i-2]=='d':
            count=count-1
        else:
            pass
    elif s[i]=='j':
        if s[i-1]=='l' or s[i-1]=='n':
            pass
        else:
            count=count+1
    else:
        count=count+1
print(count)