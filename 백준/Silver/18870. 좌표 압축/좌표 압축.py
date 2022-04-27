import sys
input=sys.stdin.readline

n=int(input().strip())
m=list(map(int,(input().strip().split())))
p=list(sorted(set(m)))

# [p.append(x) for x in m if x not in p]
# p.sort()

res={p[i]:i for i in range(len(p))}

for i in m:
    print(res[i],end=' ')

# for i in m:
#     print(p.index(i),end=' ')