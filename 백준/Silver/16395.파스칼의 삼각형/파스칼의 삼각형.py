A = list(map(int, input().split()))
mul1 = 1
mul2 = 1
mul3 = 1
A=list(map(lambda x:x-1,A))
for i in range(1, A[0]+1):
    mul1 = mul1 * i
for i in range(1, A[1]+1):
    mul2 = mul2 * i
for i in range(1, A[0]-A[1]+1):
    mul3 = mul3 * i
res = mul1/(mul2*mul3)
print(int(res))