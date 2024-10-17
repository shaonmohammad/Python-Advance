n, k = map(int, input().split())
for _ in range(k):
    last_digit = n % 10
    if last_digit != 0:
        n -= 1
    else:
        n = n / 10
print(int(n))
