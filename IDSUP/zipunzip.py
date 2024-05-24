a=['A','B','C','D']
b=[1,2,3]

z=list(zip(a,b))
print("Zipped Value is \n",z)

print("------------------------------------------------------------------------------")

print(list(zip(*z)))

a,b=list(zip(*z))
print(a)
print(b)