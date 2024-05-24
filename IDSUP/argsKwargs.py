def f1(a,b,*args):
    print(a)
    print(b)
    print(args[1])
    print(args)
    print(*args)
    print(type(args))

def f2(**Kwargs):

    # print(k1)

    print(Kwargs)
    print(*Kwargs)
    # print(**Kwargs)
    print(type(Kwargs))

f1(1,2,3,4,5)
f2(k1='raj',first='Geeks', mid='for', last='Geeks')


def myFun(arg1, arg2, arg3):
	print("arg1:", arg1)
	print("arg2:", arg2)
	print("arg3:", arg3)


# Now we can use *args or **kwargs to
# pass arguments to this function :
args = ("Geeks", "for", "Geeks")
myFun(*args)

kwargs = {"arg1": "Geeks", "arg2": "for", "arg3": "Geeks"}
myFun(**kwargs)
