def fun1(*args,**kwargs):
    print(args)
    print(kwargs)
fun1(10,20,30,name="john",email="john@example .com")

# def fun2(**kwargs, *args)     # gives error .......bcz *args should be the first argument