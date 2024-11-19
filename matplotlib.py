import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D', 'E']
values = [5, 10, 15, 20, 25]

plt.bar(categories, values, color="black", linewidth=0.5)
plt.grid(True, axis='y', color='gray', linestyle='--', linewidth=0.5)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.savefig('bar_chart.png')