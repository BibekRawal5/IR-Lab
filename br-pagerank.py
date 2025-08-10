import numpy as np

class PageRank:
    def __init__(self, pages, links, damping=0.85):
        self.pages = pages
        self.N = len(pages)
        self.damping = damping
        self.index = {page: i for i, page in enumerate(pages)}
        self.links = links
        self.M = np.zeros((self.N, self.N))


    def build_matrix(self):
        for src in self.pages:
            j = self.index[src]
            outlinks = self.links.get(src, [])
            if outlinks:
                prob = 1 / len(outlinks)
                for tgt in outlinks:
                    i = self.index[tgt]
                    self.M[i][j] = prob
            else:
                self.M[:, j] = 1 / self.N 

       

    def compute_pagerank(self, iterations=10):
        self.build_matrix()
        pr = np.array([1.0] + [0.0] * (self.N - 1))
        # print(f"Initial PR: {pr}")
        for i in range(iterations):
            pr = (1 - self.damping) / self.N + self.damping * self.M @ pr
            # print(f"Iteration {i+1}: {pr}")
        self.scores = dict(zip(self.pages, pr))


    def print_scores(self):
        print("\nFinal PageRank Scores:")
        for page, score in self.scores.items():
            print(f"{page}: {score:.4f}")


pages = ['AAA', 'BBB', 'CCC', 'DDD', 'EEE']
links = {
    'AAA': ['BBB', 'CCC'],
    'BBB': ['CCC', 'DDD'],
    'CCC': ['EEE'],
    'DDD': ['AAA'],
    'EEE': ['BBB', 'DDD']
}

pr = PageRank(pages, links, damping=0.85)
pr.compute_pagerank(iterations=2)
pr.print_scores()
