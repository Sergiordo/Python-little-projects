def add_lsts(lst1,lst2):
    lst3 = lst1 + lst2
    return sorted(lst3, reverse = True)
    
list1 = [23, 33, 5, 3, 6, 7]
list2 = [23, 5,2,5, 6, 7,343]

result = add_lsts(list1,list2)
print("Here are the lists sorted", result)