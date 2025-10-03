import matplotlib.pyplot as plt
import numpy as np

# Custom Line Graph
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.title("Sine Wave")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.savefig("lab16_line_custom.png")

# Custom Bar Chart
categories = ['A', 'B', 'C', 'D']
values = [4, 7, 1, 8]
plt.bar(categories, values)
plt.title("Category Values")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.savefig("lab16_bar_custom.png")
