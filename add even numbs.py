
def add_even(nums):
    even_nums = []
    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)
    my_sum = sum(even_nums)
    return my_sum
    
numbers = [3, 343, 6, 8, 2, 34, 34, 5]

result = add_even(numbers)
print("Here is the even numbers' sum: ", result)