s=list(input())
for i in range(len(s)):s[i]=chr(ord(s[i])+23) if (ord(s[i])-3)<65 else chr(ord(s[i])-3)
print(*s,sep='')