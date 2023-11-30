def area_square(side):
    area = side * 4
    return area
    

s = float(input("Enter a side: "))
result = area_square(s)
print("The area of the square is ", result)