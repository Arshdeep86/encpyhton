def add(num1, num2):
    sum = num1 + num2
    print(">> sum is {} ".format(sum))
add(10,20)
# Re - Defining function is not OVERLOADING in python
def add(num1, num2, num3):
    sum = num1 + num2 + num3
    print(">> sum is {} ".format(sum))
add(10,20,30)
# add(10,20)    error