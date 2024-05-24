import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
train=pd.read_csv("titanic.csv")
# print(train.head())
# print(train.isnull())
sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis')
# sns.set_style('whitegrid')
# sns.countplot(x='survived',data=train)

plt.show()

def impute_age(cols):
    age = cols[0]
    pclass = cols[1]
    if pd.isnull(age):
        if pclass == 1:
            return 37

        elif pclass == 2:
            return 29

        else:
            return 24
    else:
        return age


train['age'] = train[['age', 'pclass']].apply(impute_age, axis=1)
sns.heatmap(train.isnull(), yticklabels=False, cbar=False, cmap='viridis')
plt.show()

train.drop('cabin',axis=1,inplace=True)
sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis')
plt.show()

train.drop('fare',axis=1,inplace=True)
sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis')
plt.show()