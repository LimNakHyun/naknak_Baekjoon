scores=[]
for i in range(8):
    score=int(input())
    scores.append([i+1,score])
scores.sort(key=lambda x:x[1])
score_sum=0
for i in range(3,8):
    score_sum=score_sum+scores[i][1]
print(score_sum)
result=[]
for i in range(3,8):
    result.append(scores[i][0])
result.sort()
print(' '.join(map(str,result)))