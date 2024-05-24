str="Raj"
print(str)
# print(str[0])
# print(len(str))
# for i in range(0,len(str)):
#     print(str[i])
#
# for i in str[:]:
#     print(i)
#
# for i in str:
#     print(i)

c=0
for i in str:
    if str[i] == " ":
        c+=1
print(c)


