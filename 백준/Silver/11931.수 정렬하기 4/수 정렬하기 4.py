import sys
input=sys.stdin.readline

res=[int(input().rstrip()) for i in range(int(input().rstrip()))]
res.sort(reverse=True)
print(*res,sep='\n')