import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Example annual maximum data
years = np.array([2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009])
annual_max = np.array([10, 12, 13, 15, 14, 16, 18, 17, 19, 20])

# Perform linear regression
slope, intercept, r_value, p_value, std_err = linregress(years, annual_max)

# Print the results
print(f"Slope: {slope}")
print(f"Intercept: {intercept}")
print(f"R-squared: {r_value**2}")
print(f"P-value: {p_value}")

# Plot the data points
plt.scatter(years, annual_max, color='blue', label='Annual Maximum Data')

# Plot the trend line
trend_line = intercept + slope * years
plt.plot(years, trend_line, color='red', label='Trend Line')

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Annual Maximum')
plt.title('Trend in Annual Maximum Data')
plt.legend()

# Show the plot
plt.savefig("trend.png")