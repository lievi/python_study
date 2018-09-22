def square_numbers(nums):
    for i in nums:
        yield (i * i)


my_nums = square_numbers([1, 2, 3, 4, 5])

for num in my_nums:
    print(num)

my_comp_nums = (x * x for x in [1, 2, 3, 4, 5])
print(my_comp_nums)