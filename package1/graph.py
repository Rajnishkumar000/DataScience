import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 10)

print(x)

y = x * x
plt.plot(x, y,marker='o')
plt.show()
