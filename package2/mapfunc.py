def even_odd(n):
    if(n%2==0):
     return "The no {} is even ".format(n)
    else:
     return "The no {} is odd  ".format(n)

x=even_odd(5)
print(x)

lst=[1,2,3,4,5,6,7,8,9,10]
print(list(map(even_odd,lst)))