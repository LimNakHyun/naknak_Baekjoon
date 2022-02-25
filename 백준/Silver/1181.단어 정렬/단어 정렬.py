import sys
input=sys.stdin.readline

wn=int(input())
word_list=[]
for i in range(wn):
    word=input().rstrip()
    word_list.append(word)

res=[]
for i in set(word_list):
    res.append(i)
res.sort()
res.sort(key=len)

for i in res:
    print(i)