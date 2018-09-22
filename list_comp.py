nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Copy
mylist = [x for x in nums]

# Square list
mylist = [x * x for x in nums]

# Just even
mylist = [x for x in nums if x % 2 == 0]

# Pair for each letter and each number
mylist = [(letter, num) for letter in "abcd" for num in range(4)]

# Dict Comprehensions
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

mydict = {name: hero for name, hero in zip(names, heros)}

# Dict Comprehensions with no Peter
mydict = {name: hero for name, hero in zip(names, heros) if name != "Peter"}

nums2 = [1, 1, 2, 3, 3, 4, 6, 6, 6, 7, 8, 9, 9, 10]

# Unique values on set
my_set = {n for n in nums}

# Generator Expression
my_gen = (n * n for n in nums)
for i in my_gen:
    print(i)

print(my_set)
print(mydict)
print(mylist)
