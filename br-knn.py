import math
from collections import Counter

class KNNClassifier:
    def __init__(self, data, k=3):

        self.data = data
        self.k = k
    
    def euclidean_distance(self, v1, v2):
        return math.sqrt(sum((a - b) ** 2 for a, b in zip(v1, v2)))
    
    def classify(self, point):
        distances = []
        for features, label in self.data:
            dist = self.euclidean_distance(features, point)
            distances.append((dist, label))
        
        distances.sort(key=lambda x: x[0])
        
        k_nearest = distances[:self.k]

        labels = [label for _, label in k_nearest]
        vote_result = Counter(labels).most_common(1)[0][0]
        return vote_result


dataset = [
    ((8, 80), "High"),
    ((7, 70), "Low"),
    ((6, 65), "Low"),
    ((9, 85), "High"),
    ((8, 75), "High"),
]

knn = KNNClassifier(dataset, k=3)

new_employee = (7.5, 72)
predicted_productivity = knn.classify(new_employee)

print(f"New employee features: Work Hours={new_employee[0]}, Efficiency={new_employee[1]}")
print(f"Predicted Productivity: {predicted_productivity}")
