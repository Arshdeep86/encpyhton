file = open("stackDS.py","r")
data = file.read()   # reading the all contents of file
print(data)
print("~~~~~~~~~~~~~READING FILE UPTO 14 CHARACTER~~~~~~~~~~~~~~~~~~~~~~~~~~")
file = open("stackDS.py","r")
data = file.read(14)
print(data)
print("~~~~~~~~~~~~~~~READING FILE LINE BY LINE~~~~~~~~~~~~~~~~~~~~~~~~")
file = open("stackDS.py","r")
line1 = file.readline()
print(line1)
line2 = file.readline()
print(line2)
print("~~~~~~~~~~~~~~~~~~~READING ALL LINES FROM FILE AND CREATE LIST~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`")
file = open("stackDS.py","r")
lines = file.readlines()
functions = 0
for line in lines:
    if "def" in line:    # for searhing def word in list
        print(line)
        functions +=1
print("total functions is:",functions)