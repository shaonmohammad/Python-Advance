"""
Given a string. the task is to check if the string is symmetrical and palindrome or not.
A string is said to be symmetrical if both the halves of the string are the same and a 
string is said to be a palindrome string if one half of the string is the reverse of the 
other half or if a string appears the same when read forward or backward.
"""

def is_palindrome(str):
    is_reverse = str == str[::-1]
    is_same = str[:len(str)//2] == str[len(str)//2:]
    return True if is_reverse or is_same else False

def is_symantrical(str):
    return str[:len(str)//2] == str[len(str)//2:]
    
def main(str):
    is_palindrome(str)
    is_symantrical(str)
    return is_palindrome or is_symantrical

if __name__ == "__main__":
    input = input()
    print(main(input))
