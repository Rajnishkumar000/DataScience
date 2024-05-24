from collections import defaultdict

name="Rajnish"
title="Kumar"
print(f"name is {name} and title is {title}")

wordcount={}
document=['apple','banana','apple','cherry','apple']

# for word in document:
#     p_count=wordcount.get(word,0)
#     wordcount[word]=p_count+1
# print(wordcount)

wordcount=defaultdict(int)

for word in document:
    wordcount[word]+=1

print(wordcount)

k=[i for i in range(0,5)]
print(k)

k=[i for i in range(0,5) if i%2==0]
print(k)

l=[2,50,80,67,44,6]
k=[x+1 if x >= 45 else x+5 for x in l]
print(k)

def small(lst):
    assert lst,"empty list cannot have smallest value"
    return min(lst)

k=small([1,2])
print(k)
print("Rajnish")

