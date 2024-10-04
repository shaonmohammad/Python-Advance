#A. Lucky?
n = int(input())
for i in range(n):
    ticket = list(input())
    print("YES" if sum(list(map(int,ticket[:3]))) == sum(list(map(int,ticket[-3:]))) else "NO" )