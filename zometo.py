amount = int(input("Enter an amount: "))
if amount > 100:
    print("we have offers for you :")
    print("1. you got 40% OFF , if you pay above 200 and you apply the promocode ZOMETO")
    print("2. you got 50% OFF upto 150 , if you pay above 100 and you apply the promocode JUMBO")
    promoCode = input("Enter Promo Code: ")
    if promoCode == "ZOMATO" and amount <= 200:
        print("your amount is less than 200!!! please apply promocode ZUMBO")
    elif promoCode == "ZOMATO" and amount > 200:
        amount = amount - (0.4 * amount)
        print(">> ZOMATO Applied Successfully !! 40% OFF")
        print(">> Please Pay: \u20b9", amount)
    elif promoCode == "JUMBO":
        discount = 0.5 * amount
        if discount > 150:
            amount = amount - 150
        else:
            amount = amount - discount
        print(">> JUMBO Applied Successfully !! 50% OFF upto 150")
        print(">> Please Pay: \u20b9", amount)
else:
     print(">> Please Pay: \u20b9", amount)




