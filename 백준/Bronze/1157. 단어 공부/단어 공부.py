from collections import Counter
a=list(input().upper())
b=Counter(a).most_common()
print(b[0][0]) if len(b)==1 else print('?') if b[0][1]==b[1][1] else print(b[0][0])