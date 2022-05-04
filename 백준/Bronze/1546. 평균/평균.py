N = int(input())
scores = list(map(int, input().split()))
max_score = max(scores)
def div(x):
    return (x/max_score)*100
impo = []
impo = list(map(div, scores))
sum = 0
for i in impo:
    sum = sum + i
avg = sum / len(impo)
print(avg)