ans = []
while True:
    try:
        A, B = map(int, input().split())
        ans.append(A+B)
    except:
        break
for i in ans:
    print(i)