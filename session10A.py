# Variable Arguments in python
def add(*args):    # args can be of any name of your choice
    print(args)
    print(type(args))

    sum = 0
    for data in args:
        sum = sum + data
        print(">> sum is :",sum)
add(10,20)
add(1,2,3,4,5)

