students = ["john", "jennie", "jim", "jack", "joe"]
print(students, hex(id(students)))

newStudents = students + ["fionna", "george"]
print(newStudents, hex(id(newStudents)))

# operation --> concatenation in the same list
students = students + ["fionna", "george"]
print(students, hex(id(students)))
