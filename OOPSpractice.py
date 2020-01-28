# concept : execution of constructor ,
class counter:
    def __init__(self):
        self.count = 1
    def increment(self):
        self.count = self.count +1
    def decrement(self):
        self.count -= 1
    def ShowCount(self):
        print(">> count is: ", self.count)

c1 = counter()
c2 = counter()
c3 = c2

c1.increment()
c1.increment()
c1.increment()
c2.decrement()
c1.ShowCount()
c2.ShowCount()
c3.ShowCount()