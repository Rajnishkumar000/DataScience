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
arr = np.array([1, 2, 3, 4, 5, 6, 7])

var = arr[0:7:3]
# 1 se 5 k bich me with gap 1
print(var)