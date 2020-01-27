# Keyword arguments -> Dictionary
def fun(**kwargs):
    print(kwargs, type(kwargs))

fun(a=10, b=20, name="john")


