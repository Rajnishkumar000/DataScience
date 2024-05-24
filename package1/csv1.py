
from io import StringIO,BytesIO
import pandas as pd
import numpy as np
data=('col1,col2,col3\n'
      '2,3,1\n'
      '1,2,2\n'
      '8,9,3')
print(data)
print(type(data))
print(pd.read_csv(StringIO(data)))
df=pd.read_csv(StringIO(data),usecols=['col1','col2'])
print(df)
df.to_csv('test2.csv')
df=pd.read_csv(StringIO(data),dtype=object)
print(df)
df=pd.read_csv(StringIO(data),dtype=float)
print(df)
print(df['col2'])

data=('index1,a,b,c\n''4,apple,bat,5.7\n''8,orange,cow,10')
x=pd.read_csv(StringIO(data))
y=pd.read_csv(StringIO(data),index_col=0)
z=pd.read_csv(StringIO(data),index_col=1)
print('\n\n\n')
print(x)
print(y)
print(z)
print('\n\n\n')
data=('a,b,c\n' '4,apple,bat,\n' '8,orange,cow,')
a=pd.read_csv(StringIO(data))
print(a)


