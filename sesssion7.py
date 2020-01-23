"""""
sequences in python
Sequence : Data with quite similar type

Sequences listed below is also known as Built in data sructures here in python
tuple
list
set
dictionary
string
why data should be structured
search
filter
sort
"""""

students = ("john", "jennie","jim", "jack", "joe")
print(students)
# 1. concatenation | immutable
newStudents = students + ("fionna", "george")
print(newStudents)
print(students)
print()

# 2. Repetition
print(students*2)
print()

# 3. Membership testing
print("john" in students)
print("arsh" not in students)

# 4. Indexing
print(students[0])
print(students[len(students)-1])

# 5. Slicing
print(students[0:2])      # 0 is inclusive and 2 in exclusive
print(students[1:4])
filteredStudents = students[1:4]
print(filteredStudents)

# basic for loop
# for i in range(0, len(students)):
# print(students[i])

# Enhanced version of for loop --> For-Each loop
for student in students:
    print(student)
