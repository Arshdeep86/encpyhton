# Object is built in class in python
# By default, every class is child of object
#class Point(object):
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def showPoint(self):
        print("{} | {}".format(self.x,self.y))
    # OVERRIDING
    def __str__(self):
a# single _ (underscore) means protected in python
# double __ (underscore) means private in python
p1 = Point(10,20)
p2 = Point(30,40)

print(p1)
print(p2)
print("~~~~~~~~~~~~~~~")
print(p1.__str__())
print(p2.__str__())
