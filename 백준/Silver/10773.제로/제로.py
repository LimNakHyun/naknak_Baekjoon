import sys
input=sys.stdin.readline

k=int(input().rstrip())
stack=[]
for i in range(k):
    n=int(input().rstrip())
    if n!=0:
        stack.append(n)
    else:
        stack.pop()
print(sum(stack))