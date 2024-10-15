k, n, w = map(int, input().split())
total_cost = k * w * (w + 1) // 2
borrow = total_cost - n
print(max(0, borrow))
