import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


mu = 0      # Mean
sigma = 1   # Standard Deviation

# Create a normal distribution object
normal_dist = norm(loc=mu, scale=sigma)
x = 1.0
pdf_value = normal_dist.pdf(x)
print(f'PDF at x={x}: {pdf_value}')

x = 1.0
cdf_value = normal_dist.cdf(x)
print(f'CDF at x={x}: {cdf_value}')
p = 0.95
ppf_value = normal_dist.ppf(p)
print(f'PPF at p={p}: {ppf_value}')
num_samples = 1000
random_samples = normal_dist.rvs(size=num_samples)

# Generate values for the x-axis
x_values = np.linspace(-5, 5, 1000)

# Calculate the PDF for each x-value
pdf_values = normal_dist.pdf(x_values)

# Plot the PDF
plt.plot(x_values, pdf_values, label='PDF')
plt.title('Normal Distribution')
plt.xlabel('X')
plt.ylabel('Probability Density')
plt.legend()
plt.show()

