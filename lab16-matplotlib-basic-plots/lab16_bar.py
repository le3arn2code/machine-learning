import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
values = [4, 7, 1, 8]

plt.bar(categories, values)
plt.title("Category Values")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.savefig("lab16_bar.png")
