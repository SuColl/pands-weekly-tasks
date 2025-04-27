# this program displays: 
#  - a histogram of a normal distribution of a 1000 values with a mean of 5 
# and standard deviation of 2, 
#  - and a plot of the function  h(x)=x3 in the range 0 to 10, 
#  on the one set of axes.

# Author: Susan Collins

# import the NumPy library for array manipulation
import numpy as np
# import the MatPlotLib.PyPlot library for plotting
import matplotlib.pyplot as plt


# Parameters to generate set of 1000 normally distributed data points
distrib_mean = 5
distrib_stddev = 2
n_distrib_values = 1000

# The NumPy documentation states that the RandomState function used in 
# lectures has been superseded by the Generator method.
# This method taken from NumPy documentation - see README
# Seed the random number generator, for debugging purposes
rng = np.random.default_rng(seed=1)
# Generate set of 1000 normally distributed data points
distrib_values = rng.normal(distrib_mean, distrib_stddev, n_distrib_values)


# Cubic function parameters:
range_min = 0
range_max = 11  # set to 11 as I want to include the point x=10
index = 3
# Generate the data
x_values = np.arange(range_min,range_max)
y_values = x_values ** index


# Plot the histogram of the normally distributed data points
plt.hist(distrib_values, label="Normal distribution")
# Plot the function y=x^2, on the same plot
plt.plot(x_values,y_values, label="$y=x^3$")

# Add title and labels
# TeX symbols \mu and \sigma require double escapes inside the string.
plt.title(
    f"Histogram of Normally Distributed Data Points (n={n_distrib_values}, "
    f"$\\mu$={distrib_mean}, $\\sigma$={distrib_stddev})\n "
    f"and plot of $y=x^{index}$"
    )

plt.xlabel("X value")
plt.ylabel("Frequency of value \\ $x^3$")
plt.legend()

# Print to file
plt.savefig('histogram_and_cube_function.png')

# Display to screen
plt.show()
