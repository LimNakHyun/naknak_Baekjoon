a=input()
lit=list(a)
if a[0]=='x':
    print(1)
elif 'x' not in lit:
    print(0)
elif a[0]=='-' and a[1]=='x':
    print(-1)
else:
    print(''.join(lit[:lit.index('x')]))