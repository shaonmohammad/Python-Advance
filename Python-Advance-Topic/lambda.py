def is_odd(n): return "Yes! odd" if n % 2 != 0 else "Not Odd"


# print(is_odd(21))


# Remove degit from a string
def remove_digit(s): return ''.join([k for k in s if not k.isdigit()])


print("Remove Digit", remove_digit("abc34b222blhl3tg"))
