from collections import Counter
import sys
input=sys.stdin.readline
numbers=[]
n=int(input().strip())
for _ in range(n):
    numbers.append(int(input().strip()))
numbers.sort()

mean=int(sum(numbers))
if mean>=0:
    print(int(sum(numbers)/n+0.5))
elif mean<0:
    print(int(sum(numbers)/n-0.5))

x2=numbers[int(n/2)]
x3=Counter(numbers).most_common()
x4=numbers[-1]-numbers[0]

temp=x3[0][1]

res=[]
for i in range(len(x3)):
    if x3[i][1]==temp:
        res.append(x3[i])


print(x2)
if len(res)<2:
    print(res[0][0])
else:
    print(res[1][0])
print(x4)