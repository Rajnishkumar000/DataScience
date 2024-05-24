import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("iris.csv")
# print(df.head())
# df_setosa=df.loc[df['species']=='setosa']
# df_verginica=df.loc[df['species']=='virginica']
# df_versicolor=df.loc[df['species']=='versicolor']
# plt.plot(df_setosa['sepal_length'],np.zeros_like(df_setosa['sepal_length']),'o')
# plt.plot(df_verginica['sepal_length'],np.zeros_like(df_verginica['sepal_length']))
# plt.plot(df_versicolor['sepal_length'],np.zeros_like(df_versicolor['sepal_length']))
# sns.FacetGrid(df, hue='species').map(plt.scatter,"petal_length", "sepal_length").add_legend()
# sns.pairplot(df,hue='species',size=10)
# plt.show()
print(np.linspace(1,10,15))