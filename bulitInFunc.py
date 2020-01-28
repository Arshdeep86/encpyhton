data = [1, 2, 3, 4, 5]
print(len(data))
print(max(data))
print(min(data))

# HW : code your functions


# List comprehension
print([x**2 for x in data])

# List comprehension and Expression : error
productPrice = [123, 13562, 263, 334]

numbers = list(range(1, 101))
print(numbers)

names = ("john", "jim","jack", "joe")
names2 = list(names)
names3 = set(names)
# names4 = dict(names) | error
print(names2, type(names2))
print(names3, type(names3))