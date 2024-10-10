import math
step = [1,2,3,4]
length = int(input())
if length >= 5:
    result = math.ceil(length/5)
else:
    result = 1
print(result)