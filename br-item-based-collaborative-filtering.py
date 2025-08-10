import math
from collections import defaultdict

class ItemBasedCF:
    def __init__(self, ratings):
        self.ratings = ratings
        self.users = list(ratings.keys())
        self.items = list(next(iter(ratings.values())).keys())
        self.item_vectors = defaultdict(dict)  
        self.similarity = defaultdict(dict)    
        self._prepare_item_vectors()
        self._compute_similarities()
    
    def _prepare_item_vectors(self):
        for item in self.items:
            for user in self.users:
                rating = self.ratings[user][item]
                if rating is not None:
                    self.item_vectors[item][user] = rating
    
    def _cosine_similarity(self, item1, item2):
        users1 = set(self.item_vectors[item1].keys())
        users2 = set(self.item_vectors[item2].keys())
        common_users = users1.intersection(users2)
        if not common_users:
            return 0
        
        dot_product = sum(self.item_vectors[item1][u] * self.item_vectors[item2][u] for u in common_users)
        norm1 = math.sqrt(sum(self.item_vectors[item1][u] ** 2 for u in common_users))
        norm2 = math.sqrt(sum(self.item_vectors[item2][u] ** 2 for u in common_users))
        if norm1 == 0 or norm2 == 0:
            return 0
        return dot_product / (norm1 * norm2)
    
    def _compute_similarities(self):
        for i in range(len(self.items)):
            for j in range(i, len(self.items)):
                item1 = self.items[i]
                item2 = self.items[j]
                sim = self._cosine_similarity(item1, item2)
                self.similarity[item1][item2] = sim
                self.similarity[item2][item1] = sim
    
    def predict_rating(self, user, target_item):
        if self.ratings[user][target_item] is not None:
            return self.ratings[user][target_item]
        
        numerator = 0
        denominator = 0
        for item, rating in self.ratings[user].items():
            if rating is None or item == target_item:
                continue
            sim = self.similarity[target_item].get(item, 0)
            numerator += sim * rating
            denominator += abs(sim)
        if denominator == 0:
            return None  
        return numerator / denominator

ratings = {
    'User A': {'Laptop': 5, 'Smartphone': None, 'Tablet': 4, 'Smartwatch': 3, 'Headphones': None},
    'User B': {'Laptop': 4, 'Smartphone': 3, 'Tablet': 5, 'Smartwatch': 3, 'Headphones': 2},
    'User C': {'Laptop': 3, 'Smartphone': 5, 'Tablet': 2, 'Smartwatch': 5, 'Headphones': 4},
    'User D': {'Laptop': 5, 'Smartphone': 4, 'Tablet': 4, 'Smartwatch': 4, 'Headphones': 3},
    'User E': {'Laptop': 4, 'Smartphone': 3, 'Tablet': 5, 'Smartwatch': 4, 'Headphones': 3},
}

cf = ItemBasedCF(ratings)

pred_smartphone = cf.predict_rating('User A', 'Smartphone')
pred_headphones = cf.predict_rating('User A', 'Headphones')

print(f"Predicted rating for User A on Smartphone: {pred_smartphone:.4f}")
print(f"Predicted rating for User A on Headphones: {pred_headphones:.4f}")
