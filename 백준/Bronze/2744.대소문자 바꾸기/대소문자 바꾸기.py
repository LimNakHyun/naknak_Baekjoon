n=list(input())
for i in range(len(n)):
    if ord(n[i])<95:
        n[i]=chr(ord(n[i])+32)
    else:
        n[i]=chr(ord(n[i])-32)
print(''.join(n))