import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import matplotlib.patches as patches

# Set random seed for reproducibility
np.random.seed(42)

# Generate sample data with distinct clusters
n_samples = 300
n_centers = 4
X, y_true = make_blobs(n_samples=n_samples, centers=n_centers, 
                       cluster_std=1.2, random_state=42, center_box=(-8, 8))

# Apply K-means clustering
kmeans = KMeans(n_clusters=n_centers, random_state=42, n_init=10)
y_pred = kmeans.fit_predict(X)
centers = kmeans.cluster_centers_

# Create the plot
fig, ax = plt.subplots(1, 1, figsize=(12, 8))

# Define colors for clusters
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
center_colors = ['#E74C3C', '#1ABC9C', '#3498DB', '#27AE60']

# Plot data points without labels for legend
for i in range(n_centers):
    mask = y_pred == i
    ax.scatter(X[mask, 0], X[mask, 1], c=colors[i], alpha=0.7, s=60, 
               edgecolors='white', linewidth=0.5)

# Plot cluster centers without labels for legend
for i, center in enumerate(centers):
    ax.scatter(center[0], center[1], c=center_colors[i], s=300, 
               marker='*', edgecolors='black', linewidth=2)

# Add circles around clusters to show boundaries
for i, center in enumerate(centers):
    # Calculate approximate cluster radius
    mask = y_pred == i
    if np.sum(mask) > 0:
        distances = np.sqrt(np.sum((X[mask] - center)**2, axis=1))
        radius = np.percentile(distances, 75)  # 75th percentile for boundary
        circle = patches.Circle(center, radius, fill=False, 
                              color=center_colors[i], linewidth=2, 
                              linestyle='--', alpha=0.6)
        ax.add_patch(circle)

# Clean, minimal plot styling
ax.set_facecolor('white')

# Remove all axes, labels, ticks, and grid
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlabel('')
ax.set_ylabel('')

# Set axis limits with some padding
ax.set_xlim(X[:, 0].min() - 2, X[:, 0].max() + 2)
ax.set_ylim(X[:, 1].min() - 2, X[:, 1].max() + 2)

# Make the plot completely clean - remove all spines
for spine in ax.spines.values():
    spine.set_visible(False)

# Adjust layout and save
plt.tight_layout()
plt.savefig('kmeans_clustering_header.png', dpi=300, bbox_inches='tight', 
            facecolor='white', edgecolor='none')
plt.savefig('kmeans_clustering_header.jpg', dpi=300, bbox_inches='tight', 
            facecolor='white', edgecolor='none')

print("K-means clustering images generated successfully!")
print("Files created: kmeans_clustering_header.png and kmeans_clustering_header.jpg")

# Display some statistics
print(f"\nClustering Statistics:")
print(f"Number of data points: {n_samples}")
print(f"Number of clusters: {n_centers}")
print(f"Cluster centers:")
for i, center in enumerate(centers):
    print(f"  Cluster {i+1}: ({center[0]:.2f}, {center[1]:.2f})")
