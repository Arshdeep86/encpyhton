# operators
# arithmetic


#  code to calculate a bill of meal using arithmetic operators
dish1 = 100
dish2 = 150
#taxes = 5%

billamount = dish1 + dish2
taxes = 0.05 * billamount
billamount = taxes + billamount
print("Please pay : \u20b9", billamount)

# ** power operator
num = 2
result = num ** 3
print("two raise to power three is:", result)

# / and // operators
num1 = 100
num2 = 3
num3 = num1 / num2
print("after division num is :", num3)
num4 = num1 // num2
print("number after double division : ", num4)


#code for user input
usrinput = input("please enter something which you want to show on screen")
print("your input is :", usrinput)
#TO get integer input
intinput = int(input("please give some int value:"))
print("your integer number is:", intinput)

#Remainder operator %
number = 10
number1 = 3
remainder = 10 % 3
print("after dividing 10/3 ......Remainder is:",remainder)
