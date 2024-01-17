import matplotlib.pyplot as plt
import numpy as np

# Sample data for demonstration
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
categories = ['Category A', 'Category B', 'Category C']
values = [30, 45, 25]

# Create a figure with subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# Plot 1: Line plot
axes[0, 0].plot(x, y1, label='sin(x)', color='blue')
axes[0, 0].plot(x, y2, label='cos(x)', color='red')
axes[0, 0].set_title('Line Plot')
axes[0, 0].legend()

# Plot 2: Scatter plot
axes[0, 1].scatter(x, y1, label='sin(x)', color='green', marker='o', s=20)
axes[0, 1].set_title('Scatter Plot')
axes[0, 1].legend()

# Plot 3: Bar chart
axes[1, 0].bar(categories, values, color=['blue', 'green', 'red'])
axes[1, 0].set_title('Bar Chart')

# Plot 4: Pie chart
axes[1, 1].pie(values, labels=categories, autopct='%1.1f%%', startangle=90)
axes[1, 1].set_title('Pie Chart')

# Adjust spacing between subplots
plt.tight_layout()

# Save the figure or display it
plt.savefig('matplotlib_plots.png')  # Save the figure as an image
plt.show()  # Display the figure