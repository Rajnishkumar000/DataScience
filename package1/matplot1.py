import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 10)
y = np.arange(21, 30)
print(x)
plt.scatter(x, y, c='g')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title("Graph in 2D")
plt.show()
plt.savefig('fig1.png')
y = x * x
plt.plot(x, y)
