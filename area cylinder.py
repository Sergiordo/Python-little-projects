def area_cylinder(radius, height):
    pi = 3.14
    circle = pi * (radius **2)
    circumference = 2 * pi * radius
    rectangle = circumference * height
    total_area = (circle * 2) + rectangle
    return total_area
    
r = float(input("Enter the radius: "))
h = float(input("Enter the height: "))
result = area_cylinder(r,h)
print("The total area of a cylinder is: ", result)