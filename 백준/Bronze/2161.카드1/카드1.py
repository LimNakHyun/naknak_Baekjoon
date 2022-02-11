card=list(range(int(input()),0,-1))
result=[]
for i in range(len(card)):
    a=card.pop()
    result.append(a)
    if not card:
        break
    card=[card[-1]]+card[0:-1]
print(' '.join(str(i) for i in result))