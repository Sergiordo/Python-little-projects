def area_triangular_prism (b, h, l):
    area_triangles = 2 * (b * h / 2)
    area_rectangles = 3 * (l * b)
    area = area_triangles + area_rectangles
    print(area)
    
b = float(input("Enter the base of the equilateral triangle: "))
h = float(input("Enter the height of the equilateral triangle: "))
l = float(input("Enter the length of the prism: "))
result = area_triangular_prism(b, h, l)
print(result)
