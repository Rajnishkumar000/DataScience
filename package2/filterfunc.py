def even(num):
    return num%2==0
lst=[1,2,3,4,5,6,7,8,9,0]
print(list(filter(even,lst)))

lst=list(filter(lambda num:num%2==0,lst))
print(lst)