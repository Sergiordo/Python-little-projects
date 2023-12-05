def is_palindrome(string):
    reversed_string = string[::-1]
    if string.lower() == reversed_string.lower():
        return True
    else:
        print("This is not a palindrome.")
        return False

test = "Anna"
result = is_palindrome(test)
print(result)
