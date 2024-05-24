import pandas as pd
import matplotlib as plt
data = {
    'Category': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C'],
    'Value_1': [10, 15, 8, 12, 9, 7, 11, 14, 6],
    'Value_2': [25, 18, 20, 22, 16, 19, 23, 17, 21]
}

df = pd.DataFrame(data)

# You can use this DataFrame with Seaborn for various data visualization tasks.
print(df)
print(df.head())