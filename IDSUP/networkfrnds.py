from  collections import  defaultdict
from itertools import count

students = [
 { "id": 0, "name": "Rahul" },
 { "id": 1, "name": "Ashok" },
 { "id": 2, "name": "Sarita" },
 { "id": 3, "name": "Piyus" },
 { "id": 4, "name": "Puja" },
 { "id": 5, "name": "Harish" },
 { "id": 6, "name": "Rohan" },
 { "id": 7, "name": "Sunil" },
 { "id": 8, "name": "Rajesh" },
 { "id": 9, "name": "Amlan" },

]
student_pairs = [(0, 1), (0, 2), (1, 2), (1,
3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7),
(6, 8), (7, 8), (8, 9)]

friend_net=defaultdict(list)
for i, j in student_pairs:
    friend_net[i].append(j)
    friend_net[j].append(i)


print(dict(friend_net))

# print(sorted(f.values(),key=lambda x1: (len(x1),len(x2))))

# newd={}
# def countlen(friend_net):
#  for i in friend_net:
#   newd[i]=len(friend_net[i])
#  return newd
#
# newd=countlen(dict(friend_net))
#
# sorted_dict = dict(sorted(newd.items(), key=lambda item: item[1]))
# print(sorted_dict)




print(friend_net.items())
print("\n\n\n")
print(dict(sorted(friend_net.items(),key=lambda x:len(x[1]))))


# x = lambda y: y[4]
# print(x(friend_net))









