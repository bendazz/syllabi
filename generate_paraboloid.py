import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Create figure with white background
fig = plt.figure(figsize=(12, 8))
fig.patch.set_facecolor('white')
ax = fig.add_subplot(111, projection='3d')
ax.set_facecolor('white')

# Define colors matching the syllabus theme
surface_color = '#2c3e50'
edge_color = '#34495e'

# Create paraboloid data
x = np.linspace(-3, 3, 50)
y = np.linspace(-3, 3, 50)
X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2  # Paraboloid equation z = x² + y²

# Create the surface plot
surf = ax.plot_surface(X, Y, Z, alpha=0.8, cmap='Blues', 
                      linewidth=0.1, edgecolors=edge_color,
                      antialiased=True)

# Customize the plot for a clean, professional look
ax.set_xlabel('')
ax.set_ylabel('')
ax.set_zlabel('')

# Remove tick labels for cleaner appearance
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_zticklabels([])

# Set viewing angle for best appearance
ax.view_init(elev=25, azim=45)

# Remove the grid
ax.grid(False)

# Remove the axes
ax.set_axis_off()

# Adjust layout to remove margins
plt.tight_layout()
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)

# Save the image
plt.savefig('paraboloid_visualization.png', dpi=300, bbox_inches='tight', 
            facecolor='white', edgecolor='none')
plt.savefig('paraboloid_visualization.jpg', dpi=300, bbox_inches='tight', 
            facecolor='white', edgecolor='none')

print("Paraboloid visualization saved as: paraboloid_visualization.png, paraboloid_visualization.jpg")
