def area_cone(radius, height):
    pi = 3.14
    circle = pi * (radius **2)
    circumference = 2 * pi * radius
    rectangle = circumference * height
    area_cylinder = (circle * 2) + rectangle
    area_cone = area_cylinder / 3
    return area_cone
    
r = float(input("Enter the radius: "))
h = float(input("Enter the height: "))
result = area_cone(r,h)
print("The total area of the cone is: ", result)
