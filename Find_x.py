#This funtion will find the value of 'x' given an equation where we know the result and the coefficient.

def find_x(equation_result, coefficient):
    x = equation_result / coefficient
    return x

result = find_x(20, 4)

print(result)
