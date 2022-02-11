n=int(input())
ball=1
for i in range(n):
    a,b=map(int,input().split())
    if b==ball:
        ball=a
    elif a==ball:
        ball=b
print(ball)