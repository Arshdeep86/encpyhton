# Standardization of class data
class customer:
    def __init__(self, name, phone, email, gender, address):
        print("Init is executed")
        print(">> self is : ", self)
        self.name = name
        self.phone = phone
        self.email = email
        self.gender = gender
        self.address = address

    def ShowCustomerDetails(self):
        print("{} can be called at {} and lived in {}, for email {}".format(self.name, self.phone, self.address,self.email))


c1 = customer("fionna","+91 98364743436","fionna@example.com","female","redwood shores")
c2 = customer("john","+91 981485624358","john@example.com","male","USA")
c1.ShowCustomerDetails()
c2.ShowCustomerDetails()

