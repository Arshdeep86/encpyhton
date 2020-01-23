#built in API


name = "arsh"
print(name, id(name))
name.upper() # string cant modified
print(name, id(name))
newname = name.upper()
print(newname)


authorName = "john watson"
print(authorName, id(authorName))
# authorName = authorName.capitalize()  # here we create new string and referring it to old variable authorName
# print(authorName, id(authorName))

# for memory optimization
somename = authorName.capitalize()
del authorName
print(somename, id(somename))
# print(authorName, id(authorName))   # err

names = "john, jennie, jim, jack, joe"
print(names[0])
print(names[len(names)-1])
idx = names.index("jennie")
print(idx)

newnames = names.replace('j', 'k')
print(newnames)

num = names.count("j",0,len(names))
print(num)









