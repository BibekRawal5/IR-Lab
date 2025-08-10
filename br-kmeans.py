import math
import random

class KMeans:
    def __init__(self, points, k=2, max_iters=100):
        self.points = points
        self.k = k
        self.max_iters = max_iters
        self.centroids = []
        self.clusters = [[] for _ in range(k)]
    
    def euclidean_distance(self, p1, p2):
        return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
    
    def initialize_centroids(self):
        self.centroids = random.sample(self.points, self.k)
    
    def assign_clusters(self):
        self.clusters = [[] for _ in range(self.k)]
        for point in self.points:
            distances = [self.euclidean_distance(point, centroid) for centroid in self.centroids]
            min_index = distances.index(min(distances))
            self.clusters[min_index].append(point)
    
    def update_centroids(self):
        new_centroids = []
        for cluster in self.clusters:
            if len(cluster) == 0: 
                new_centroids.append(random.choice(self.points))
                continue
            x_mean = sum(p[0] for p in cluster) / len(cluster)
            y_mean = sum(p[1] for p in cluster) / len(cluster)
            new_centroids.append((x_mean, y_mean))
        return new_centroids
    
    def fit(self):
        self.initialize_centroids()
        for i in range(self.max_iters):
            old_centroids = self.centroids
            self.assign_clusters()
            self.centroids = self.update_centroids()
            # Stop iterations
            if all(math.isclose(c[0], o[0], abs_tol=1e-4) and math.isclose(c[1], o[1], abs_tol=1e-4) 
                   for c, o in zip(self.centroids, old_centroids)):
                break
    
    def print_clusters(self):
        for i, cluster in enumerate(self.clusters):
            print(f"Cluster {i+1}:")
            for point in cluster:
                print(f"  {point}")
            print(f"Centroid: {self.centroids[i]}")
            print()


customers = [
    (2, 3),
    (3, 4),
    (5, 8),
    (6, 8),
    (8, 8),
    (9, 9),
    (1, 2),
    (4, 6),
]

kmeans = KMeans(customers, k=2)
kmeans.fit()
kmeans.print_clusters()
