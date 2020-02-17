import threading
lock = threading.Lock()
class MovieTicket:
    def __init__(self,name,seatNum):
        self.name = name
        self.seatNum = seatNum
        self.IsBooked = False
    def ShowMovieTicket(self):
        print("Ticket Details : {} | {} | {} ".format(self.name,self.seatNum,self.IsBooked))
m1 = MovieTicket("love aaj kal",1)
m2 = MovieTicket("love aaj kal",2)
m3= MovieTicket("love aaj kal",3)
m4 = MovieTicket("love aaj kal",4)
m5 = MovieTicket("love aaj kal",5)
rowA = [m1, m2, m3, m4, m5]

class BookMovieTicket(threading.Thread):
    def SelectMovieTicket(self,ticket,email):
        self.ticket =ticket
        self.email = email

    def run(self):
        lock.acquire()
        if self.ticket.IsBooked == False:
            print("Booking for {} ".format(self.email))
            print("Movie Ticket book for {} ".format(self.email))
            for i in range(0,10):
                print("Procession Payments for {} ".format(self.email))
                self.ticket.IsBooked = True
                print("Email sent to {}".format(self.email))
                self.ticket.ShowMovieTicket()
                print("________________________________________")
            else:
                print("sorry !! Ticket not available !!")
        lock.release()
def main():
    print(">>App started")
    user1 = BookMovieTicket()
    user2 = BookMovieTicket()
    user1.SelectMovieTicket(rowA[1], "john@example.com")
    user2.SelectMovieTicket(rowA[1], "fionna@example.com")
    user1.start()
    user2.start()
    print(">>App finished")

if __name__ == '__main__':
    main()