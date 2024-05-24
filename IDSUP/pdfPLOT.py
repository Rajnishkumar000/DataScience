# import numpy as np
# import matplotlib.pyplot as plt
#
# # Parameters
# mu = 1
# sigma = 6
#
# # Generate x values
# x = np.linspace(-20, 22, 1000)
#
# # Calculate the Normal PDF
# pdf = 1/(sigma * np.sqrt(2 * np.pi)) * np.exp(-(x - mu)*2 / (2 * sigma*2))
#
# # Plot the Normal PDF
# plt.plot(x, pdf,'-',label='Normal PDF')
# plt.xlabel('x')
# plt.ylabel('Probability Density')
# plt.title('Normal Probability Density Function (μ=1, σ=6)')
# plt.legend()
# plt.grid(True)
# plt.show()





import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Generate some data points
x = np.linspace(-5, 5, 1000)
# Calculate the probability density function (PDF) using a normal distribution
pdf = norm.pdf(x, loc=0, scale=1)

# Plot the PDF with a dotted line
plt.plot(x, pdf, linestyle='solid', label='PDF')
plt.xlabel('X')
plt.ylabel('Probability Density')
plt.title('Probability Density Function')
plt.legend()
plt.grid(True)
plt.show()
