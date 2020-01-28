"""
In python there is no funtion overloading, if we create a function with same name the old one gets deleteda and new
function is created


UPDATING DATA IN OBJECTS, WE CREATE ANOTHER FUNCTION
"""

class customer:
    def __init__(self, name,phone,email,gender, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.gender = gender
        self.address = address

    def UpdateCustomerDetails(self,name,phone,email,gender,address):
        self.name = name
        self.phone = phone
        self.email = email
        self.gender = gender
        self.address = address
    def ShowCustomerDetails(self):
        print("{} can be lived in {} and called at {} ".format(self.name,self.address,self.phone))


    # upgrade object data with new attributes other than init method
    def UpgradeToPrime(self,customerType,wallet):
        self.customerType = customerType
        self.wallet = wallet

    def ShowPrimeCustomerDetails(self):
        print("{} can be {} type of customer".format(self.name,self.customerType))
        print("wallet is : \u20b9",self.wallet)


c1 = customer("john","+91 589643","john@example.com","male","brumpton")
c1.ShowCustomerDetails()

# updating the objects data
c1.UpdateCustomerDetails("john watson","+91 589660","johnwatson@example.com","male","brumpton")
c1.ShowCustomerDetails()
c1.UpgradeToPrime("Prime",100)
c1.ShowPrimeCustomerDetails()

# Reference copy operation,  c2 contains same data as c1 contain , both refer to same hashcode
c2 = c1
c2.ShowPrimeCustomerDetails()