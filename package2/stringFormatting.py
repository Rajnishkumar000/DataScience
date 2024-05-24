def func(name):
    print("Hello {}. Welcome to the community ".format(name))

func("Rajnish")


def email(firstname,lastname):
    print("Welcome {}. Everyone please Welcome {} ".format(firstname,lastname)) #ORDERING IS IMPORTANT

email("Rajnish","Kumar")


def name_age(name,age):
    print("Welcome {name}. Your age is  {age} ".format(name=name,age=age))

name_age("Rajnish",20)


def name_age(name,age):
    print("Welcome {name1}. Your age is  {age1} ".format(age1=age,name1=name))

name_age("Rajnish",20)