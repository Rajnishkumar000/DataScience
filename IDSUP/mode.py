from collections import counter
def mode(lst):
    c=counter(lst)
    print(c.items)

mode([1,2,3,1,2,3,4,2])