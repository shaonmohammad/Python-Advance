a = " abc def gh "
print(a)
# print(a[::-1])  # reverse the string using slicing

#String Immutability
# a[0] = 'X'  # this will show a TypeError

b = " a" + a[2:]
print(b)

# Replace
b = b.replace("a","X")
print(b)

# Remove Space
b = b.strip()
print(b)

#Using f-strings
name = "Alice"
age = 22
print(f"Name: {name}, Age: {age}")


# Join Mehtod
join_str = map(str,input("Enter the time with format %D:%M:%Y: ").split())
result = "-".join(list(join_str))
print(result)