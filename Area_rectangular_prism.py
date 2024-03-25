def area_rectangular_prism (w, l, h):
    area = 2 * (w*l + w*h + l*h)
    print(area)
    
w = float(input('enter the length of the width: '))
l = float(input('enter the length of the lentgh: '))
h = float(input('enter the length of the height: '))
result = area_rectangular_prism(w, l, h)
