# Regular Expressions
import re
quote = "Search the candle rather than cursing the darkness"
#result = re.match("Search",quote)  # 0-6
#result = re.match("candle",quote)  # None
#result = re.search("the",quote)
result = re.findall("the",quote)

print(result,type(result))
print("_________________________________")
#data = re.split("the", quote)
data = re.sub("the","a",quote)
print(data,type(data))