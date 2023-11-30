def factorial(num):
    result = 1
    while num > 1:
        result *= num
        num -= 1
    return result

# Example usage:
number = 5
result = factorial(number)
print(f"The factorial of {number} is: {result}")