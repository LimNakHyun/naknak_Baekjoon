from itertools import permutations
n=int(input())
for i in list(permutations([i+1 for i in range(n)],n)):print(i[0]) if i==1 else print(*i)