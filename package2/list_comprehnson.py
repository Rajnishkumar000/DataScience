from numpy import append

lst=[]
def lst_square(lst1):

    for i in lst1:
        lst.append(i*i)
    return lst


myList=[1,2,3,4,5,6,7,8]
print(lst_square(myList))

# USING LIST COMPREHNSON
print([i*i for i in myList if i%2==0])