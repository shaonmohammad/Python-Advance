import re

mystring = 'My name afat uddin shaon'
match = re.search(r'afat', mystring)

# print('Start Index', match.start())
# print('End index', match.end())


# 1. \ – Backslash
name = 'afat.uddin'
# if we use only (.) then it give me any matching character.if i want to to find exactly the value then i have to use (\) before the (.)
search = re.search(r'\.', name)
# print(search)


# 2. [] – Square Brackets
company = "My company name is Mediusware Ltd."
pattern1 = "[^a-c]"
search1 = re.findall(pattern1, company)
# print(search1)


# 3. ^ – Caret
regex = r"^This"
strings = ['This is a book', 'This is my first interview',
           'I am a software Enginner']
for string in strings:
    if re.match(regex, string):
        pass
        # print("Matched:", string)
    else:
        pass
        # print("Not Matched:", string)


# 4. $ – Dollar
# $ is totaly oposite of caret(^).it just check if any character end with any particular pattern or character.


# 5. . – Dot
strings = [
    # Matches
    "john.a@gmail.com",
    "john1@yahoo.com",
    "john_d@outlook.com",
    "john-5@abc.com",
    "johnx@company.org",

    # Non-matches
    "john@gmail.com",  # Missing a character between "john" and "@"
    "johnny@xyz.com",  # Extra characters after "john"
    "john@domain.com",  # No character between "john" and "@"
    "john.a@",  # Incomplete email
    "john.a@.com"  # No valid character after "@"
]
pattern2 = r"john.@."
# Testing each string
for string in strings:
    if re.search(pattern2, string):
        pass
        # print(f"Match: {string}")
    else:
        pass
        # print(f"Not match: {string}")
