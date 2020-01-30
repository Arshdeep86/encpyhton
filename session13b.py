class Product:
    def __init__(self,pid,name,price,quantity):
        self.pid = pid
        self.name = name
        self.price = price
        self.quantity = quantity
        self.nextProduct = None
        self.prevProduct = None

    def showProductDetails(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("{}\t{}\t{}".format(self.pid,self.name,self.price))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

class LinkedList:
    def __init__(self):
        print("linked list created")
        print(self)
        self.head = None
        self.current = None

    def append(self,product):
        print(product)
        if self.head == None:
            self.head = product
            self.current = product
        else:
            product.prevProduct = self.current
            self.current.nextProduct = product
            self.current = product
            product.nextProduct = self.head

    def IterateForward(self):
        temp = self.head
        while temp.nextProduct != self:
            temp.showProductDetails()
            temp = temp.nextProduct
        temp.showProductDetails()

    def getTotalPrice(self):

        totalPrice = 0
        totalItems = 0
        totalProducts = 0

        temp = self.head

        while temp.nextProduct != self.head:
            totalPrice = totalPrice + (temp.price * temp.quantity)
            totalItems = totalItems + temp.quantity
            totalProducts += 1
            temp = temp.nextProduct

        totalPrice = totalPrice + (temp.price * temp.quantity)
        totalItems = totalItems + temp.quantity
        totalProducts += 1

        return (totalPrice, totalItems, totalProducts)


shoppingCart = LinkedList()
#product1 = Product(101,"iphoneX",70000)
#shoppingCart.append(product1)

shoppingCart.append(Product(101,"iphoneX",70000,1))
shoppingCart.append(Product(201,"shoes",3000,2))
shoppingCart.append(Product(301,"samsung LED",40000,1))

result = shoppingCart.getTotalPrice()
print(">> TOTAL PRICE:\u20b9", result[0])
print(">> TOTAL ITEMS:", result[1])
print(">> TOTAL PRODUCTS:", result[2])




































































