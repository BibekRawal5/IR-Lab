from collections import defaultdict
import math

class UserBasedCF:
    def __init__(self, ratings):
        self.ratings = ratings
        self.users = list(ratings.keys())
        self.books = list(next(iter(ratings.values())).keys())
    
    def pearson_correlation(self, user1, user2):
        # find common books rated
        common_books = [book for book in self.books
                        if self.ratings[user1][book] is not None and self.ratings[user2][book] is not None]
        print(f"Common books between {user1} and {user2}: {common_books}")
        n = len(common_books)
        if n == 0:
            return 0 
        
        sum1 = sum(self.ratings[user1][book] for book in common_books)
        sum2 = sum(self.ratings[user2][book] for book in common_books)
        
        sum1_sq = sum(self.ratings[user1][book]**2 for book in common_books)
        sum2_sq = sum(self.ratings[user2][book]**2 for book in common_books)
        
        product_sum = sum(self.ratings[user1][book] * self.ratings[user2][book] for book in common_books)
        
        numerator = product_sum - (sum1 * sum2 / n)
        denominator = math.sqrt((sum1_sq - sum1**2 / n) * (sum2_sq - sum2**2 / n))
        if denominator == 0:
            return 0
        return numerator / denominator
    
    def predict_rating(self, target_user, target_book):
        similarities = {}
        for user in self.users:
            if user == target_user or self.ratings[user][target_book] is None:
                continue
            sim = self.pearson_correlation(target_user, user)
            if sim > 0:  
                similarities[user] = sim
        print(f"Similarities for {target_user}: {similarities}")
        if not similarities:
            user_ratings = [r for r in self.ratings[target_user].values() if r is not None]
            return sum(user_ratings) / len(user_ratings) if user_ratings else None
        
        # weighted average ratings by others
        numerator = 0
        denominator = 0
        for user, sim in similarities.items():
            numerator += sim * self.ratings[user][target_book]
            denominator += abs(sim)
        
        if denominator == 0:
            return None
        return numerator / denominator


ratings = {
    'User A': {'Book 1': 5, 'Book 2': None, 'Book 3': 3, 'Book 4': 4, 'Book 5': None},
    'User B': {'Book 1': 4, 'Book 2': 3, 'Book 3': 4, 'Book 4': 3, 'Book 5': 2},
    'User C': {'Book 1': 2, 'Book 2': 5, 'Book 3': 1, 'Book 4': 5, 'Book 5': 4},
    'User D': {'Book 1': 4, 'Book 2': 4, 'Book 3': 3, 'Book 4': 5, 'Book 5': 3},
    'User E': {'Book 1': 3, 'Book 2': 3, 'Book 3': 4, 'Book 4': 4, 'Book 5': 2},
}

cf = UserBasedCF(ratings)
predicted = cf.predict_rating('User A', 'Book 2')
print(f"Predicted rating for User A on Book 2: {predicted:.4f}")
