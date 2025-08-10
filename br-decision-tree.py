import math
from collections import defaultdict, Counter

class SimpleDecisionTree:
    def __init__(self, dataset):
        self.dataset = dataset
        self.features = [f for f in dataset[0] if f != 'label']
    
    def entropy(self, data_subset):
        total = len(data_subset)
        if total == 0:
            return 0
        label_counts = Counter([d['label'] for d in data_subset])
        ent = 0
        for count in label_counts.values():
            p = count / total
            ent -= p * math.log2(p)
        return ent
    
    def info_gain(self, feature):
        total_entropy = self.entropy(self.dataset)
        total = len(self.dataset)

        subset_1 = [d for d in self.dataset if d[feature] == 1]
        subset_0 = [d for d in self.dataset if d[feature] == 0]

        ent_1 = self.entropy(subset_1)
        ent_0 = self.entropy(subset_0)

        weighted_entropy = (len(subset_1)/total) * ent_1 + (len(subset_0)/total) * ent_0

        gain = total_entropy - weighted_entropy
        return gain
    
    def build_tree(self):

        gains = {}
        for f in self.features:
            gains[f] = self.info_gain(f)
        
        best_feature = max(gains, key=gains.get)
        return best_feature, gains[best_feature]

data = [
    {'win':1, 'offer':1, 'meeting':0, 'label':'Spam'},
    {'win':0, 'offer':0, 'meeting':1, 'label':'Not Spam'},
    {'win':0, 'offer':1, 'meeting':0, 'label':'Spam'},
    {'win':0, 'offer':0, 'meeting':1, 'label':'Not Spam'},
]

dt = SimpleDecisionTree(data)

initial_entropy = dt.entropy(data)
print(f"Initial Entropy of dataset: {initial_entropy:.4f}")

info_gain_offer = dt.info_gain('offer')
print(f"Information Gain for splitting on 'offer': {info_gain_offer:.4f}")

info_gain_win = dt.info_gain('win')
print(f"Information Gain for splitting on 'win': {info_gain_win:.4f}")

best_feature, gain = dt.build_tree()
print(f"Best feature to split on: '{best_feature}' with Information Gain = {gain:.4f}")
