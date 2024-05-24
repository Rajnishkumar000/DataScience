import seaborn as sns
import matplotlib.pyplot as plt

# Sample data in lists
DData = [10, 15, 20, 25, 30, 35, 40, 45, 50]

# Create a Seaborn plot
sns.set(style="whitegrid")  # Set the style of the plot
sns.histplot(DData, kde=True)  # Create a histogram with a kernel density estimate

# Show the plot
# df=sns.load_dataset("data")
# print(df)
plt.show()
