# this program displays: 
#  - a histogram of a normal distribution of a 1000 values 
# with a mean of 5 and standard deviation of 2, 
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
cubic_range_min = 0
cubic_range_max = 11  # set to 11 as I want to include the point x=10
index = 3
# Generate the data
x_values = np.arange(cubic_range_min,cubic_range_max,1)
y_values = x_values ** index


# Calculate the histogram bin limits.
# I want to centre a bin on each integer value. I need to find the  
# centre of the lowest bin and the centre of the highest bin.

# Subtract 0.5 from min & max to round down
lowest_bin_centre = round(min(distrib_values))
highest_bin_centre = round(max(distrib_values))

# Generate list of bin edges as floats
integer_bins = np.arange(lowest_bin_centre - 0.5, highest_bin_centre + 0.5, 1)


# Plot the histogram of the normally distributed data points
plt.hist(
    distrib_values, bins=integer_bins, label="Normal distribution", 
    color="cyan", edgecolor = "white"
    )


# Plot the function y=x^3, on the same plot
plt.plot(
    x_values,y_values, label="$y=x^3$", color="m", 
    marker="o", markersize=3, linewidth=0.5
    )

# Add title and labels
# TeX symbols \mu and \sigma require double escapes inside the string.
plt.title(
    f"Histogram of Normally Distributed Data Points (n={n_distrib_values}, "
    f"$\\mu$={distrib_mean}, $\\sigma$={distrib_stddev})\n "
    f"and plot of $y=x^{index}$"
    )

plt.xlabel("X value")
plt.ylabel(f"Frequency of value \\ $x^{index}$")
plt.legend()

# set x-axis ticks be integer values that range from the lowest value in 
# either plot, to the highest value in either plot.
x_axis_minimum = min(lowest_bin_centre, round(cubic_range_min)-1)
x_axis_maximum = max(highest_bin_centre, round(cubic_range_max)+1)
plt.xticks(range(x_axis_minimum, x_axis_maximum, 1))

# Print to file
plt.savefig('histogram_and_cube_function.png')

# Display to screen
plt.show()

