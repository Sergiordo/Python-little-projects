my_list = [23, 4445, 2, 5454, 565, 4232, 1, 4]

def average(lst):
    sum_of_elements = sum(lst)
    avg = sum_of_elements / len(lst)
    return avg

result = average(my_list)
print("Average:", result)