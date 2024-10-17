player = input()
count = 1

for i in range(1, len(player)):
    if player[i] == player[i-1]:
        count += 1
        if count == 7:
            print("YES")
            break
    else:
        count = 1
else:
    print("NO")
