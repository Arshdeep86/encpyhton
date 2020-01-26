number = "100"
print("is this digit:", number, number.isdigit())    # true when string contain digits

audioFile = "abc.mp3"
print("this file is mp3? ", audioFile,)
x = audioFile.endswith("mp3")   # true if string end with mp3
print(x)

txt = "arsh125"
y = txt.isalnum()  # true if string is alphanumeric
print(y)

abc = "arhsdeep"
z = abc.isalpha()
print(z)

xyz = "2525"
a = xyz.isdecimal()
print(a)

A = "arsh"
b = "some_one"
c = "rohit_12"
d = "is arsh"
e = "--abc"
f = "1xyz"
g = "__@#$"
print("arsh is valid identifier :", A.isidentifier())    # returns true  if string is valid identifier
print("some_one is valid identifier :", b.isidentifier())
print("rohit_12 is valid identifier :", c.isidentifier())
print("is arsh is valid identifier :", d.isidentifier())
print("--abc is valid identifier :", e.isidentifier())
print("1xyz is valid identifier :", f.isidentifier())
print("__@#$ is valid identifier :", g.isidentifier())
print()

i = "india"
print("i is lower:",i.islower())
j = "123"
print(" j is numeric:", j.isnumeric())
k = "ARSH"
print("k is in upper case:", k.isupper())


