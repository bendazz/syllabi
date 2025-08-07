import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# Set random seed for reproducibility
np.random.seed(42)

# Generate sample data
n_samples = 300
X, _ = make_blobs(n_samples=n_samples, centers=4, n_features=2, 
                  random_state=42, cluster_std=1.5)

# Apply K-means clustering
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
y_kmeans = kmeans.fit_predict(X)

# Create the plot
plt.figure(figsize=(10, 6))

# Define colors for each cluster
colors = ['red', 'blue', 'green', 'orange']

# Plot ONLY the data points colored by cluster (no centroids)
for i in range(4):
    cluster_points = X[y_kmeans == i]
    plt.scatter(cluster_points[:, 0], cluster_points[:, 1], 
                c=colors[i], alpha=0.7, s=50)

# Remove axes, ticks, and labels for clean appearance
plt.axis('off')

# Remove any padding/margins
plt.tight_layout()
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)

# Save the image
plt.savefig('kmeans_clustering_header.jpg', dpi=300, bbox_inches='tight', 
            pad_inches=0, facecolor='white')
plt.close()

print("K-means clustering header image (without centroids) saved as 'kmeans_clustering_header.jpg'")
