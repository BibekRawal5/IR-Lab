import numpy as np

class HITS:
    def __init__(self, influencers, citations):
        self.influencers = influencers
        self.index = {name: i for i, name in enumerate(influencers)}
        self.adj_matrix = np.zeros((len(influencers), len(influencers)))  # A[i][j] = 1 if i cites j
        self._build_adjacency(citations)
    
    def _build_adjacency(self, citations):
        for citer, cited_list in citations.items():
            for cited in cited_list:
                self.adj_matrix[self.index[citer]][self.index[cited]] = 1
    
    def run_hits(self, iterations=3):
        n = len(self.influencers)
        authority = np.ones(n)
        hub = np.ones(n)

        for it in range(iterations):
            new_authority = np.dot(self.adj_matrix.T, hub)
            new_hub = np.dot(self.adj_matrix, new_authority)

            # Normalize
            authority = new_authority / np.linalg.norm(new_authority)
            hub = new_hub / np.linalg.norm(new_hub)

        self.authority_scores = dict(zip(self.influencers, authority))
        self.hub_scores = dict(zip(self.influencers, hub))
    
    def print_scores(self):
        print("Final Authority Scores:")
        for k, v in self.authority_scores.items():
            print(f"{k}: {v:.4f}")

        print("\nFinal Hub Scores:")
        for k, v in self.hub_scores.items():
            print(f"{k}: {v:.4f}")
    
    def top_influencers(self):
        top_authority = max(self.authority_scores, key=self.authority_scores.get)
        top_hub = max(self.hub_scores, key=self.hub_scores.get)
        return top_authority, top_hub


# Sample Data
influencers = ['X', 'Y', 'Z', 'W']
citations = {
    'X': ['Y', 'Z'],
    'Y': ['Z', 'W'],
    'Z': ['X', 'W'],
    'W': ['X']
}

hits = HITS(influencers, citations)
hits.run_hits(iterations=3)
hits.print_scores()

top_auth, top_hub = hits.top_influencers()
print(f"\nTop Authority: {top_auth}")
print(f"Top Hub: {top_hub}")
