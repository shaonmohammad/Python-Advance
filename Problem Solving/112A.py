# A. Petya and Strings
str1 = input().split()
str2 = input().split()
str1 = [s.lower() for s in str1]
str2 = [s.lower() for s in str2]

if str1 > str2:
    print("1")
elif str1 == str2:
    print("0")
else:
    print("-1")
