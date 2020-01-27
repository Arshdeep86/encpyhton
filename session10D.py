"""def maxNumbers(data):
    max = data[0]
    for num in data:
        if num > max:
            max = num
    return max
numbers = [10,25,30,40]
print(">> Max number in {} is {} ".format(numbers,maxNumbers(numbers))) """

"""def maxnumbers(data,length):
    if length == 1:
        return data[0]
    else:
        num = maxnumbers(data, length-1)
    if num > data[length-1]:
        return num
    else:
        return data[length-1]

numbers = [10,30,40]
print(">> max is : ", maxnumbers(numbers, 3)) """


def binary(num):
    if num == 0:
        return num
    else:
        binary(num // 2)
        print((num % 2), end=" ")

number = 8
(binary(number))


