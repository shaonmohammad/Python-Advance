n = int(input())
s = list(input())
A_count = 0
D_count = 0
for i in s:
    if i == "A":
        A_count += 1
    else:
        D_count += 1
if A_count > D_count:
    print("Anton")
elif A_count < D_count:
    print("Danik")
else:
    print("Friendship")
