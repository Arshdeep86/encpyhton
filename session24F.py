import threading
import requests
class PrintingTask(threading.Thread):
    def printingDetails(self,name,copies):
        self.name = name
        self.copies = copies
    def run(self):
        for i in range(1,self.copies+1):
            print(">> Printing {} copy # {}".format(self.name,i))
def main():
    print(">>App started")
    task = PrintingTask()
    task.printingDetails("abc.pdf",5)
    task.start()
    for i in range(1,11):
        print(">> i is",i)
    print((">>App finished"))
if __name__ == '__main__':
    main()


