a = 5
b = 6
c = 2
binOfa = bin(a)
print("binary of a is: ", binOfa)
binOfb = bin(b)
print("binary of b is: ", binOfb)

res = a & b             #if both bits are 1 then give 1 otherwise 0
print("after binary and is : ",res)
binofres = bin(res)
print("binary of res is after and operation: ", binofres)

res = a | b             #if one of the  bits is 1 then give 1 otherwise 0
print("after binary or is : ",res)
binofres = bin(res)
print("binary of res is after and operation: ", binofres)

res = a ^ b             #if both bits are diff then give 1 otherwise 0
print("after binary XOR is : ",res)
binofres = bin(res)
print("binary of res is after and operation: ", binofres)

print(binOfa)
res = ~ a          #negation of the bits
print("after binary negation is : ",res)
binofres = bin(res)
print("binary of res is after and operation: ", binofres)






