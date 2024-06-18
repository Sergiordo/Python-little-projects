def volume_cone(radius, height):
    pi = 3.14
    area_base = pi * (radius **2)
    volume_cylinder = (area_base) * height
    volume_cone = volume_cylinder / 3
    return volume_cone
    
r = float(input("Enter the radius: "))
h = float(input("Enter the height: "))
result = volume_cone(r,h)
print("The total volume of the cone is: ", result)
