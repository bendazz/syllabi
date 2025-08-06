import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import numpy as np

# Create figure with white background
fig, ax = plt.subplots(1, 1, figsize=(12, 8))
fig.patch.set_facecolor('white')
ax.set_facecolor('white')

# Define colors matching the syllabus theme
node_color = '#2c3e50'
leaf_color = '#3498db'
line_color = '#34495e'

# Tree structure parameters
root_x, root_y = 0.5, 0.85
level_spacing = 0.2
node_width = 0.08
node_height = 0.06

# Helper function to draw a node
def draw_node(x, y, is_leaf=False):
    color = leaf_color if is_leaf else node_color
    circle = plt.Circle((x, y), 0.03, color=color, zorder=3)
    ax.add_patch(circle)

# Helper function to draw a line
def draw_line(x1, y1, x2, y2):
    ax.plot([x1, x2], [y1, y2], color=line_color, linewidth=2, zorder=1)

# Draw the decision tree
# Root node
draw_node(root_x, root_y)

# Level 1 nodes
left_1 = root_x - 0.25
right_1 = root_x + 0.25
y_1 = root_y - level_spacing

draw_line(root_x, root_y, left_1, y_1)
draw_line(root_x, root_y, right_1, y_1)
draw_node(left_1, y_1)
draw_node(right_1, y_1)

# Level 2 nodes (left side)
left_2_1 = left_1 - 0.15
left_2_2 = left_1 + 0.15
y_2 = y_1 - level_spacing

draw_line(left_1, y_1, left_2_1, y_2)
draw_line(left_1, y_1, left_2_2, y_2)
draw_node(left_2_1, y_2, is_leaf=True)  # Leaf node
draw_node(left_2_2, y_2)

# Level 2 nodes (right side)
right_2_1 = right_1 - 0.15
right_2_2 = right_1 + 0.15

draw_line(right_1, y_1, right_2_1, y_2)
draw_line(right_1, y_1, right_2_2, y_2)
draw_node(right_2_1, y_2, is_leaf=True)  # Leaf node
draw_node(right_2_2, y_2, is_leaf=True)  # Leaf node

# Level 3 nodes (from the remaining internal node)
left_3_1 = left_2_2 - 0.1
left_3_2 = left_2_2 + 0.1
y_3 = y_2 - level_spacing

draw_line(left_2_2, y_2, left_3_1, y_3)
draw_line(left_2_2, y_2, left_3_2, y_3)
draw_node(left_3_1, y_3, is_leaf=True)  # Leaf node
draw_node(left_3_2, y_3, is_leaf=True)  # Leaf node

# Remove axes and clean up
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Remove all margins and padding
plt.tight_layout()
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)

# Save the image
plt.savefig('simple_decision_tree.png', dpi=300, bbox_inches='tight', 
            facecolor='white', edgecolor='none')
plt.savefig('simple_decision_tree.jpg', dpi=300, bbox_inches='tight', 
            facecolor='white', edgecolor='none')

print("Simple decision tree visualization saved as: simple_decision_tree.png, simple_decision_tree.jpg")
