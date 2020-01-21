# passing references | as value
def sqaure(num):
    num = num * num
    print("num is : ", num, id(num))    # gives 100

num = 10      # num is reference variable which holds hashcode
print(">> num is :", num, id(num))      # gives 10
sqaure(num)
print(">>  now num is :", num, id(num))      # gives 10