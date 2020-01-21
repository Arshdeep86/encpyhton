
def sqaure (numbers):
    print(">>[sqaure] numbers is :", numbers, id(numbers))
    for i in range(0, len(numbers)):
        numbers[i] = numbers[i] * numbers[i]
        print(numbers[i], id(numbers[i]))

# List in python
numbers = [10, 20, 30, 40, 50]
print(">>[main] numbers is :", numbers, type(numbers), id(numbers))
for i in range(0, len(numbers)):
    print(numbers[i], id(numbers[i]))

sqaure(numbers)
print(">>[main] numbers is :", numbers, type(numbers), id(numbers))
for i in range(0, len(numbers)):
    print(numbers[i], id(numbers[i]))


