# A. Bit++

n = int(input())
result = 0
for i in range(n):
    operation = input()
    if operation == '++X' or operation == 'X++':
        result += 1
    elif operation == '--X' or operation == 'X--':
        result -= 1

print(result)
