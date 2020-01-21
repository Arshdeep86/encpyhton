# creating a show functions
def show(num):
    if num == 0:
        return    # its an acknowledge statement
    print(">> num is:", num)
    num -= 1  # num = num-1
    show(num)    #  recursion in function
#execution of function
show(10)
