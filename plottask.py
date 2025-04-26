# this program displays: 
#  - a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
#  - and a plot of the function  h(x)=x3 in the range 0 to 10, 
#  on the one set of axes.

# Author: Susan Collins

# import the NumPy library for array manipulation
import numpy as np
# import the MatPlotLib.PyPlot library for plotting
import matplotlib.pyplot as plt


# Parameters for set of 1000 normally distributed data points
distrib_mean = 5
distrib_stddev = 2
n_distrib_values = 1000

# The NumPy documentation states that the RandomState function used in lectures has be superseded by the Generator method.
# This method taken from https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.choice.html
# Seed the random number generator, for debugging purposes
rng = np.random.default_rng(seed=1)
# Generate set of 1000 normally distributed data points
distrib_values = rng.normal(distrib_mean, distrib_stddev, n_distrib_values)


# Print to test
print(distrib_values)
