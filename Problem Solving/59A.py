s = input()
list = list(s)
upper_count = 0
lower_count = 0
for i in list:
    if i.isupper():
        upper_count += 1
    else:
        lower_count += 1
print((s.upper()) if upper_count > lower_count else s.lower())
