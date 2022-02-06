import sys
N = int(input())
X = []
for i in range(N):
    A, B = map(int, sys.stdin.readline().split())
    X.append(A+B)
for i in X:
    print(i)