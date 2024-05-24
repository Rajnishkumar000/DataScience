#List is iterator

lst=[1,2,3,4,5,6,7,8,9]
for i in lst:
    print(i)


list1=iter(lst)
print(list1)

print(next(list1))
print(next(list1))
print(next(list1))
print(next(list1))
print(next(list1))
print()
print()
print()

list2=[11,13,14,15,16,17]
list3=iter(list2)
print(next(list3))
print(next(list3))
print(next(list3))
print(next(list3))
print()
print()
print()

list4=[23,24,25,26]
# print(next(list4))WILL THROW AN ERROR



#FOR LOOP USING ITERATOR
lst5=[2,4,6,8,10,12]

lst6=iter(lst5)
# print(next(lst6))
for i in lst6:
    print(i)
#benefit of iterator is it does not initialise the whole list at once so it is easy to work with big dataset