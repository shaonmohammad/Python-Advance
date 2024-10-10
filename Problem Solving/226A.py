n = int(input())
stone = input()[:n]
total = 0
for i in range(n-1):
    if stone[i] == stone[i+1]:
        total += 1
print(total)
