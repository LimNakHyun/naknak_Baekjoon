from sys import stdin
input = stdin.readline 
a=[]
for _ in range(int(input())):a.append(list(map(int,input().split())))
a.sort(key=lambda k:(k[0],k[1]))
for b in a:print(*b,sep=' ')