print(">> Welcome to Pyhton App")

num = 5
print(">> 1. num is :", num)

def square(n):
    #global num    it will print num =49 after executing 15 line number
    n = n*n
    num = n
    print(">> 2. n is :", n)
    print(">> 3. num is:", num)
    #  return ... last statement of function is always return

square(7)
print(">> 4. num is :", num)