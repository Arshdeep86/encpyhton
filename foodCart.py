class Dish:
    def __init__(self,name,price,description, type):
        self.name = name
        self.price = price
        self.description = description
        self.type = type
        self.quantity = 0

    def showDishsetails(self):
        print("{}\t{}\t{}\t{}\t{}".format(self.name,self.price,self.description,self.type,self.type))
        print("======================")


dish1 = Dish("Dal makhni",200,"Black Lentils Cooked Overnight","indian veg")
dish2 = Dish("paneer makhni",300,"paneer wala makhan","indian veg")
dish3 = Dish("burger",100,"tikki wala burger","indian veg")
dish4 = Dish("noodels",200,"desi noodels","desi chinese")
dish5 = Dish("manchurian",300,"round manchurian","desi chinese")

cart = []
totalDishes = 0


def addDishtoCart(dish):
    global totalDishes
    cart.append(dish)
    totalDishes = totalDishes + 1


dish1.quantity = 1
dish2.quantity = 5
addDishtoCart(dish1)
addDishtoCart(dish2)

totalPrice = 0
totalItems = 0
for dish in cart:
    dish.showDishsetails()
    totalPrice += (dish.price*dish.quantity)
    totalItems += dish.quantity

print(">> Total Price:\u20b9", totalPrice)
print(">> Total Items:", totalItems)
print(">> Total Dishes:", totalDishes)


