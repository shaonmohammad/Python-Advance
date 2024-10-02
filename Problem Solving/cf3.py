# A. Team

n = int(input())

result = 0
for i in range(n):
    is_sure = list(map(int, input().split()))
    count = 0
    for k in is_sure:
        if k == 1:
            count += 1
    if count > 1:
        result += 1
print(result)


