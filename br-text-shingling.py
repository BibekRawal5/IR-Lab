class TextShingling:
    def __init__(self, doc1, doc2, k=3):
        self.doc1 = doc1.lower().split()
        self.doc2 = doc2.lower().split()
        self.k = k
    
    def get_shingles(self, words):
        shingles = set()
        for i in range(len(words) - self.k + 1):
            shingle = ' '.join(words[i:i+self.k])
            shingles.add(shingle)
        return shingles
    
    def jaccard_similarity(self, set1, set2):
        intersection = set1.intersection(set2)
        union = set1.union(set2)
        if not union:
            return 0.0
        return len(intersection) / len(union)
    
    def compare(self):
        shingles1 = self.get_shingles(self.doc1)
        shingles2 = self.get_shingles(self.doc2)
        
        similarity = self.jaccard_similarity(shingles1, shingles2)
        
        print("Shingles in Document 1:")
        print(shingles1)
        print("\nShingles in Document 2:")
        print(shingles2)
        print(f"\nJaccard Similarity (k={self.k}): {similarity:.4f}")

D1 = "Data science is fascinating and growing rapidly"
D2 = "Data science is evolving and growing rapidly"

shingling = TextShingling(D1, D2, k=3)
shingling.compare()
