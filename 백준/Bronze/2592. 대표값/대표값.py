from collections import Counter
a=[int(input()) for _ in range(10)]
print(sum(a)//10)
print(Counter(a).most_common()[0][0])