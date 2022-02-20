count=0
max_count=0
for _ in range(4):
    a,b=map(int,input().split())
    count=count-a+b
    if count>max_count:
        max_count=count
print(max_count)