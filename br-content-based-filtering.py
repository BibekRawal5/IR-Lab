import math

class ContentBasedRecommender:
    def __init__(self, songs):
        self.songs = songs
    
    def cosine_similarity(self, v1, v2):
        dot = sum(a*b for a,b in zip(v1, v2))
        norm1 = math.sqrt(sum(a*a for a in v1))
        norm2 = math.sqrt(sum(b*b for b in v2))
        if norm1 == 0 or norm2 == 0:
            return 0
        return dot / (norm1 * norm2)
    
    def recommend(self, preferred_song):
        if preferred_song not in self.songs:
            return None
        
        preferred_vector = self.songs[preferred_song]
        similarities = {}
        
        for song, features in self.songs.items():
            if song == preferred_song:
                continue
            sim = self.cosine_similarity(preferred_vector, features)
            similarities[song] = sim
        
        if not similarities:
            return None
        
        recommended_song = max(similarities, key=similarities.get)
        return recommended_song, similarities[recommended_song]


songs = {
    'Song A': (1.0, 0.8, 0.5, 0.7),
    'Song B': (0.9, 0.7, 0.6, 0.6),
    'Song C': (0.8, 0.6, 0.7, 0.8),
    'Song D': (0.7, 0.9, 0.4, 0.9),
    'Song E': (0.6, 0.5, 0.8, 0.5),
}

recommender = ContentBasedRecommender(songs)
song, similarity = recommender.recommend('Song A')

print(f"Recommended song similar to 'Song A': {song} (Similarity: {similarity:.4f})")
