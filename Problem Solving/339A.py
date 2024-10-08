math = input()
num_list = sorted(list(map(int, math.replace('+', ''))))
result = "+".join(str(s) for s in num_list)
print(result)
