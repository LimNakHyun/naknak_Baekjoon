import sys
input=sys.stdin.readline

n=int(input().rstrip())
lis=[int(input().rstrip()) for i in range(n)]
lis.sort()
print(" ".join(str(i) for i in lis))