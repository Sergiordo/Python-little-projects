def is_palindrome(string):
    reversed_string = string[::-1]
    if string == reversed_string:
        return True
    else:
        print("This is not a palindrome.")
        return False

test = "sggis"
result = is_palindrome(test)
print(result)