import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = 2 * x

plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()