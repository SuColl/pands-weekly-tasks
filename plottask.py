# this program displays: 
#  - a histogram of a normal distribution of 1000 values 
# with a mean of 5 and standard deviation of 2, 
#  - and a plot of the function  h(x)=x3 in the range 0 to 10, 
#  on the one set of axes.

# Author: Susan Collins

# import the NumPy library for array manipulation
try:
    import numpy as np
except ModuleNotFoundError:
    print(
        "This program requires the module 'NumPy'.\n"
        "Please install this module and try again. \nGoodbye."
    )
    exit()

# import the MatPlotLib.PyPlot library for plotting
try:
    import matplotlib.pyplot as plt
except ModuleNotFoundError:
    print(
        "This program requires the module 'MatPlotLib'.\n"
        "Please install this module and try again. \nGoodbye."
    )
    exit()


# Parameters to generate set of normally distributed data points
distrib_mean = 5
distrib_stddev = 2
n_distrib_values = 1000

# The NumPy documentation states that the RandomState function used in 
# lectures has been superseded by the Generator method.
# This method taken from NumPy documentation - see README
# Seed the random number generator, for debugging purposes
rng = np.random.default_rng(seed=1)
# Generate set of normally distributed data points
distrib_values = rng.normal(distrib_mean, distrib_stddev, n_distrib_values)


# Cubic function parameters:
cubic_range_min = 0
cubic_range_max = 10 
index = 3
# Generate the data over many points
x_values = np.arange(cubic_range_min,cubic_range_max,0.001)
y_values = x_values ** index


# Calculate the histogram bin limits.
# I want bins of width 1 and to centre a bin on each integer value.
# I need to find the centre of the lowest bin 
# and the centre of the highest bin.
lowest_bin_centre = round(min(distrib_values))
highest_bin_centre = round(max(distrib_values))

# Generate list of bin edges as floats
integer_bins = np.arange(lowest_bin_centre-0.5, highest_bin_centre+0.5, 1)


########## Building the plot
# use subplots() to get access to the Axes object.
# An Axes object encapsulates all the elements of an 
# individual (sub-)plot in a figure.
fig, ax1 = plt.subplots()


# Plot the histogram of the normally distributed data points on first Axes
ax1.hist(
    distrib_values, bins=integer_bins, label="Normal distribution", 
    color="aqua", edgecolor = "white"
    )
ax1.set_xlabel("X-values")
ax1.set_ylabel("Frequency", color="aqua")
ax1.tick_params(axis='y', labelcolor="aqua")
# make sure y-axis starts at 0 - must call this after plotting the data
ax1.set_ylim(bottom = 0)


# create second Axes object that has the same x-axis as the first 
ax2 = ax1.twinx()

# Plot the function h(x)=x^3, on the second Axes
ax2.plot(
    x_values,y_values, label="$h(x)=x^3$", color="red", 
    linewidth=1.2
    )
ax2.set_ylabel(f"$h(x)=x^{index}$", color="red")
ax2.tick_params(axis='y', labelcolor="red")
# make sure y-axis starts at 0 - must call this after plotting the data
ax2.set_ylim(bottom = 0)


# set x-axis ticks be integer values that range from the lowest value in 
# either plot, to the highest value in either plot.
x_axis_minimum = min(lowest_bin_centre, round(cubic_range_min)-1)
x_axis_maximum = max(highest_bin_centre, round(cubic_range_max)+1)
plt.xticks(range(x_axis_minimum, x_axis_maximum, 1))


# Add main title and legend
# Use figure object to title and legend the entire plot (both Axes)
# TeX symbols \mu and \sigma require double escapes inside the string.
fig.suptitle(
    f"Histogram of Normally Distributed Data Points (n={n_distrib_values}, "
    f"$\\mu$={distrib_mean}, $\\sigma$={distrib_stddev})\n "
    f"and plot of $h(x)=x^{index}$"
)

fig.legend(
    loc="upper left", bbox_to_anchor=(0, 1), bbox_transform=ax1.transAxes
)

fig.tight_layout()  # otherwise the right y-label is slightly clipped

# Print to file
plt.savefig('histogram_and_cube_function.png')

# Display to screen
plt.show()

