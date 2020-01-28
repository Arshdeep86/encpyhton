"""
    Types Of Recursion
    1. Direct Recursion
    2. Indirect Recusrion
    3. Tail Recursion
"""
def factorial(n):     # Direct recursion
   if n == 1:
       return n
   else:
       return n*factorial(n-1)

print("The factorial is",factorial(5))


