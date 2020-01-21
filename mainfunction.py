# here we have control over the program, if we call main then main is executed otherwise not
# print(__name__)
def show():
    num = 20
    print(">>num is:", num)
def main():
    num = 10
    print(">> this is awesome main")
    show()
    print(" this last statement of main function")

if __name__ == "__main__":
    main()