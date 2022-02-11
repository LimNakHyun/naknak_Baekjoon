n=int(input())
cute=[int(input()) for i in range(n)]
if sum(cute)>len(cute)-cute.count(1):
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')