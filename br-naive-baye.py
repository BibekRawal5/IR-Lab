import math
from collections import defaultdict, Counter

class NaiveBayesClassifier:
    def __init__(self, dataset):
        self.dataset = [(review.lower(), label) for review, label in dataset]
        self.vocab = set()
        self.class_word_counts = defaultdict(Counter)  
        self.class_doc_counts = defaultdict(int)       
        self.total_docs = len(dataset)
        self.class_probs = {}   
        self.word_probs = {}    
        self._build_model()
    
    def _build_model(self):
        for review, label in self.dataset:
            self.class_doc_counts[label] += 1
            words = review.split()
            for word in words:
                self.vocab.add(word)
                self.class_word_counts[label][word] += 1
        
        for cls in self.class_doc_counts:
            self.class_probs[cls] = self.class_doc_counts[cls] / self.total_docs
        
        self.class_total_words = {cls: sum(words.values()) for cls, words in self.class_word_counts.items()}
        self.vocab_size = len(self.vocab)
    
    def _word_likelihood(self, word, cls):
        #Laplace smoothing
        word_count = self.class_word_counts[cls][word] if word in self.class_word_counts[cls] else 0
        return (word_count + 1) / (self.class_total_words[cls] + self.vocab_size)
    
    def classify(self, text):
        text = text.lower()
        words = text.split()
        class_scores = {}
        
        for cls in self.class_probs:
            log_prob = math.log(self.class_probs[cls])
            for word in words:
                log_prob += math.log(self._word_likelihood(word, cls))
            class_scores[cls] = log_prob
        
        return max(class_scores, key=class_scores.get)


dataset = [
    ("The movie is fantastic", "Positive"),
    ("I love this movie", "Positive"),
    ("The plot is terrible", "Negative"),
    ("I hate this movie", "Negative")
]

nb = NaiveBayesClassifier(dataset)

new_review = "The movie is excellent"
predicted_class = nb.classify(new_review)

print(f'Review: "{new_review}"')
print(f'Classified as: {predicted_class}')
