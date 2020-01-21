# program to accept order , and give discount to customer based on promocode and amount condition, and suggest
# promocode to customer

def order(amount, promocode):
    if amount > 100 and promocode == "JUMBO":
        discount = 0.5 * amount
        if discount > 150:
            amount = amount - 150
        else:
            amount = amount - discount
            print("Jumbo code apply successfully !! 50% OFF upto 150")
            print("please pay : \u20b9", amount)
    elif amount > 200 and promocode == "ZOMATO":
        amount = amount - (0.4 * amount)
        print("ZOMATO applied successfully ...40% off")
        print("please pay: \u20b9", amount)
    elif amount < 200 and promocode == "ZOMATO":
        print("your amount is less than 200......please apply JUMBO to get 50% off upto 150")
    else:
        print("please pay: \u02b9", amount)
order(220,"ZOMATO")


    












