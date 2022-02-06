n=int(input())
bi=format(n,'b')
print(int(''.join(reversed(str(bi))),2))