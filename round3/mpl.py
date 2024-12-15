import matplotlib.pyplot as plt
import numpy as np

# Arrays for method ID (x-axis) and priority (y-axis)
x = np.array([30, 31, 32, 33])  # method id
y = np.array([10, 5, 1, 7])     # priority values

# Plotting the data
plt.plot(x, y, marker='o', linestyle='-', color='b')  # Plot x vs y

# Labeling the axes
plt.xlabel("Method ID")
plt.ylabel("Priority")
plt.xticks(np.arange(min(x), max(x)+1, 1))
plt.show()