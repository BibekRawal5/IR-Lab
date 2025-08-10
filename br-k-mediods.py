import math
import random

class KMedoids:
    def __init__(self, points, k=2, max_iters=100):
        self.points = points
        self.k = k
        self.max_iters = max_iters
        self.medoids = []
        self.clusters = [[] for _ in range(k)]
    
    def euclidean_distance(self, p1, p2):
        return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
    
    def initialize_medoids(self):
        self.medoids = random.sample(self.points, self.k)
    
    def assign_clusters(self):
        self.clusters = [[] for _ in range(self.k)]
        for point in self.points:
            distances = [self.euclidean_distance(point, medoid) for medoid in self.medoids]
            min_index = distances.index(min(distances))
            self.clusters[min_index].append(point)
    
    def update_medoids(self):
        new_medoids = []
        for cluster in self.clusters:
            if len(cluster) == 0:
                new_medoids.append(random.choice(self.points))
                continue
            
            total_distances = []
            for candidate in cluster:
                dist_sum = sum(self.euclidean_distance(candidate, other) for other in cluster)
                total_distances.append((dist_sum, candidate))
            
            new_medoid = min(total_distances, key=lambda x: x[0])[1]
            new_medoids.append(new_medoid)
        return new_medoids
    
    def fit(self):
        self.initialize_medoids()
        for i in range(self.max_iters):
            old_medoids = self.medoids
            self.assign_clusters()
            self.medoids = self.update_medoids()
            # Stop iterations (condition)
            if set(self.medoids) == set(old_medoids):
                break
    
    def print_clusters(self):
        for i, cluster in enumerate(self.clusters):
            print(f"Cluster {i+1}:")
            for point in cluster:
                print(f"  {point}")
            print(f"Medoid: {self.medoids[i]}\n")


warehouses = [
    (2, 6),  
    (3, 4),  
    (5, 8),  
    (6, 2),  
    (8, 4),  
    (7, 6),  
    (4, 7),  
]

kmedoids = KMedoids(warehouses, k=2)
kmedoids.fit()
kmedoids.print_clusters()
