A = [3, 8, 9, 7,6]
R = 3
# Output [9,7,6,3,8]
newList = A.pop(0)
print(newList)
A.append(newList)
newList = A.pop(0)
A.append(newList)
print(A)
