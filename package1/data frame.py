import pandas as pd
import numpy as np
# intialise data of lists.
data = {'Name': ['Tom', 'nick', 'krish', 'jack'],
        'Age': [20, 21, 19, 18]}

# Create DataFrame
# df = pd.DataFrame(data)
df=pd.DataFrame(np.arange(0,20).reshape(5,4),index=["Row1","Row2","Row3","Row4","Row5"],columns=["coloumn1","coloumn2","coloumn3","coloumn4"])
print(df)

df.to_csv("test1.csv")
print(df.loc['Row1'])
print(type(df.loc['Row1']))
print(df.iloc[0:2,0:2])

print(type(df.iloc[0:2,0:2]))
print(df.iloc[0:2,0])
print(type(df.iloc[0:2,0]))
print((df.iloc[1:4,:].values))
print((df.iloc[1:4,:].values.shape))

print("     ")
print("     ")
print("     ")
print("     ")
df=pd.read_csv('test1.csv')
print(df.head())
print("     ")
print("     ")
print(df.info())
print("     ")
print("     ")
print("     ")

