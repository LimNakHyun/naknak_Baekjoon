import sys
input = sys.stdin.readline
n=int(input())
stack=[]
for i in range(n):
    a=input().rstrip()
    if 'push'in a:
        b=a
        b=b.split()
        stack=stack+[b[-1]]
    elif a=='pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()
    elif a=='top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
    elif a=='size':
        print(len(stack))
    elif a=='empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    else:
        pass