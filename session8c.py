names = "john, joe, jack, jim"
spliitedNames = names.split(",")
print("after Splitting names are : ", spliitedNames)


for name in spliitedNames:  # to show names in different lines
    print(name.strip())

quotes = """Work Hard, Get Luckier
Search the Candle, rather than cursing the darkness
"""
words = quotes.split(" ")  # split the quotes into words through spaces
for word in words:         # print each word in new line
    print(word)

