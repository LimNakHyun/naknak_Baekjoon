from sys import stdin
input=stdin.readline

tmp='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

a,n=map(int,input().strip().split())
ans=''

while a!=0:
    ans+=str(tmp[a%n])
    a=a//n

print(ans[::-1])