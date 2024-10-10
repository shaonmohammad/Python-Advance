letters = input()
vowel = ['a', 'e', 'i', 'o', 'u','y']  
result = ''.join(f".{letter.lower()}" for letter in letters if letter.lower() not in vowel)
print(result)
