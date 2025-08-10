from collections import defaultdict
import math

class RocchioClassifier:
    class_vectors = defaultdict(list)
    
    def __init__(self, documents):
        self.documents = documents
        self.classes = set(cls for cls, _ in documents)
    
    def compute_centroids(self):
        sums = defaultdict(lambda: [0.0, 0.0])
        counts = defaultdict(int)
        
        for cls, vec in self.documents:
            sums[cls][0] += vec[0]
            sums[cls][1] += vec[1]
            counts[cls] += 1
        
        self.centroids = {}
        for cls in self.classes:
            self.centroids[cls] = (sums[cls][0] / counts[cls], sums[cls][1] / counts[cls])
    
    def euclidean_distance(self, v1, v2):
        return math.sqrt((v1[0] - v2[0])**2 + (v1[1] - v2[1])**2)
    
    def classify(self, vector):
        min_dist = float('inf')
        predicted_class = None
        
        for cls, centroid in self.centroids.items():
            dist = self.euclidean_distance(vector, centroid)
            if dist < min_dist:
                min_dist = dist
                predicted_class = cls
        
        return predicted_class

docs = [
    ('China', (0.8, 0.1)),
    ('China', (0.7, 0.2)),
    ('UK', (0.2, 0.7)),
    ('UK', (0.3, 0.8)),
    ('Kenya', (0.1, 0.4)),
    ('Kenya', (0.2, 0.5)),
]

classifier = RocchioClassifier(docs)
classifier.compute_centroids()

doc7 = (0.3, 0.6)
predicted_class = classifier.classify(doc7)

print("Class centroids:")
for cls, centroid in classifier.centroids.items():
    print(f"{cls}: {centroid}")

print(f"\nDoc7 {doc7} is classified as: {predicted_class}")
