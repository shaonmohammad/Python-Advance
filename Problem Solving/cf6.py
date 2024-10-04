# A. Next Round

n, k = map(int, input().split())
result = 0
score = list(map(int, input().split()))
target = score[k-1]

for i in score:
    if i >= target and i > 0:
        result = result + 1
print(result)
