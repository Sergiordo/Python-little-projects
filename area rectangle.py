def area_rectangle(length, width):
    if length <= width:
        print("The length must be longer than the width.")
        return None  
    area = length * width
    return area

l = float(input("Enter a length: "))
w = float(input("Enter a width: "))

result = area_rectangle(l, w)

if result is not None:
    print("The area of the rectangle is:", result)