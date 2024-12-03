number = int(input())
extract_digit = []
while number > 0:
    digit = number % 10
    extract_digit.append(digit)
    number //= 10

# Count lucky digits (4 and 7)
lucky_count = 0
for d in extract_digit:
    if d == 4 or d == 7:  # Corrected condition
        lucky_count += 1

# Check if lucky_count is a lucky number
is_nearly_lucky = lucky_count == 4 or lucky_count == 7

if is_nearly_lucky:
    print("YES")
else:
    print("NO")
