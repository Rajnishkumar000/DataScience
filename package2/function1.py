num=24
if num%2==0:
    print("no is even")
else:
    print("the no is odd")

def func(name , age):
    print("my name is {} and my age is {}".format(name,age))
func("rajnish",20)





def func(name , age=21):
    print("my name is {} and my age is {}".format(name,age))
func("rajnish",20)


def func(name , age=22):
    print("my name is {} and my age is {}".format(name,age))
func("rajnish")


def func(name="raju" , age=22):
    print("my name is {} and my age is {}".format(name,age))
func("rajnish",45)


def hello(*a,**b):
    print(a)
    print(b)

hello("raj","nish"," kumar",age=23,str="am good",str1="too much")

lst=["my name is raj","and i am good"]
dictona={'age':29,'dob':1990}

hello(lst,dictona) #here both will pass as positional arguement so to pass as of both we have to put * and **
hello(*lst,**dictona)
