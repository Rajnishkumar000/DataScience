import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as mlt
df=pd.read_csv("iris.csv")
print(df.head())
print(df.shape)
print(df.loc[df['species']=='setosa'])
df_setosa=df.loc[df['species']=='setosa']
df_verginica=df.loc[df['species']=='virginica']
df_versicolor=df.loc[df['species']=='versicolor']