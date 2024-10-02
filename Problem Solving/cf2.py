# A. Way Too Long Words


n = int(input())

for i in range(0, n):
    word = input()
    if len(word) > 10:
        print(f"{word[0]}{len(word)-2}{word[-1]}")
    else:
        print(word)
