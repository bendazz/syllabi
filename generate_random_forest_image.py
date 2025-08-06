import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
import numpy as np

# Set up the figure
fig, ax = plt.subplots(1, 1, figsize=(14, 8))

# Colors
tree_color = '#2c3e50'
leaf_color = '#3498db'
bg_color = '#ecf0f1'
accent_color = '#e74c3c'

# Set background color
fig.patch.set_facecolor('white')
ax.set_facecolor('white')

# Title
ax.text(0.5, 0.95, 'Random Forest Ensemble', 
        horizontalalignment='center', verticalalignment='center',
        transform=ax.transAxes, fontsize=20, fontweight='bold', 
        color=tree_color)

# Function to draw a simple decision tree
def draw_tree(ax, x_center, y_center, width=0.15, height=0.3, tree_num=1):
    # Root node
    root = FancyBboxPatch((x_center - width/6, y_center + height/2), 
                         width/3, height/8,
                         boxstyle="round,pad=0.01", 
                         facecolor=tree_color, edgecolor='black', linewidth=1.5)
    ax.add_patch(root)
    
    # Root node text
    ax.text(x_center, y_center + height/2 + height/16, f'Feature {tree_num}', 
            ha='center', va='center', fontsize=8, color='white', fontweight='bold')
    
    # Internal nodes (level 2)
    for i, x_offset in enumerate([-width/3, width/3]):
        node = FancyBboxPatch((x_center + x_offset - width/8, y_center + height/6), 
                             width/4, height/10,
                             boxstyle="round,pad=0.008", 
                             facecolor=tree_color, edgecolor='black', linewidth=1)
        ax.add_patch(node)
        
        # Connect to root
        ax.plot([x_center, x_center + x_offset], 
                [y_center + height/2, y_center + height/6 + height/20], 
                'k-', linewidth=2)
    
    # Leaf nodes (level 3)
    leaf_positions = [-width/2, -width/6, width/6, width/2]
    for i, x_offset in enumerate(leaf_positions):
        leaf = FancyBboxPatch((x_center + x_offset - width/12, y_center - height/6), 
                             width/6, height/12,
                             boxstyle="round,pad=0.005", 
                             facecolor=leaf_color, edgecolor='black', linewidth=1)
        ax.add_patch(leaf)
        
        # Connect to internal nodes
        parent_x = x_center + [-width/3, -width/3, width/3, width/3][i]
        ax.plot([parent_x, x_center + x_offset], 
                [y_center + height/6, y_center - height/6 + height/24], 
                'k-', linewidth=1.5)

# Draw 5 trees in the forest
tree_positions = [0.15, 0.325, 0.5, 0.675, 0.85]
for i, x_pos in enumerate(tree_positions):
    draw_tree(ax, x_pos, 0.5, tree_num=i+1)

# Add "Random Sampling" annotations
ax.text(0.5, 0.15, 'Each tree trained on random subset of data and features', 
        horizontalalignment='center', verticalalignment='center',
        transform=ax.transAxes, fontsize=12, style='italic', color=tree_color)

# Add voting/aggregation visualization
# Draw arrows pointing to final prediction
for x_pos in tree_positions:
    ax.annotate('', xy=(0.5, 0.05), xytext=(x_pos, 0.25),
                xycoords='axes fraction', textcoords='axes fraction',
                arrowprops=dict(arrowstyle='->', color=accent_color, lw=2))

# Final prediction box
final_box = FancyBboxPatch((0.45, 0.02), 0.1, 0.06,
                          boxstyle="round,pad=0.01", 
                          facecolor=accent_color, edgecolor='black', linewidth=2)
ax.add_patch(final_box)
ax.text(0.5, 0.05, 'Final\nPrediction', 
        horizontalalignment='center', verticalalignment='center',
        transform=ax.transAxes, fontsize=10, fontweight='bold', color='white')

# Add labels for each tree
for i, x_pos in enumerate(tree_positions):
    ax.text(x_pos, 0.25, f'Tree {i+1}', 
            horizontalalignment='center', verticalalignment='center',
            transform=ax.transAxes, fontsize=10, fontweight='bold', color=tree_color)

# Add "Majority Vote" or "Average" label
ax.text(0.5, 0.1, 'Majority Vote (Classification)\nor Average (Regression)', 
        horizontalalignment='center', verticalalignment='center',
        transform=ax.transAxes, fontsize=10, color=accent_color, fontweight='bold')

# Remove axes
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Save the figure
plt.tight_layout()
plt.savefig('/workspaces/syllabi/random_forest_visualization.png', 
            dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
plt.savefig('/workspaces/syllabi/random_forest_visualization.jpg', 
            dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')

print("Random Forest visualization saved as:")
print("- random_forest_visualization.png")
print("- random_forest_visualization.jpg")

plt.show()
