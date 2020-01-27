"""
OOPS : object Oriented programming Structure
      how we design software
      Its methodology
 1. Object
 2. Class

Real world :
object : anything which exists in Realaity
class : represent how an object will look like
      : Drawing of an object

        Principle of OOPS
        1. think od object
        2. create its class
        3. From class create real object

computer science :
object : Multi value container
        Homogeneous/ Hetro
        data in object is stored as Dictionary
        where keys are known as attributes which will hold values as data
class : Represent how an object will look like
       what it should contain as data
       provide certain functionalities to process the data as well in object

       Principle of OOPS
        1. think od object
            we need analyze detailed requirements from client regarding his/her software needs. Identify
            all those terms which will have lot of data associated with it
            that term -> object and data associated -> attributes
        2. create its class
        3. From class create real object

"""
# creating a class
class Customer:
    pass
# from class create real object
#object construction statement
cRef = Customer()
print("cRef is :", cRef)
print("type of cRef:", type(cRef))
print("hashcode of cRef : ", id(cRef))
print("cRef dictionary", cRef.__dict__)

#  Add data in object
cRef.name = "john Watson"
cRef.phone = "+91 7634872364823"
cRef.email = "john@example.com"

# update data in object
cRef.phone = "156464"

# delete data in object
#del cRef.name

# delete an object
del cRef
print("cRef dictionary", cRef.__dict__)
