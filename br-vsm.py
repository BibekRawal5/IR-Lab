from collections import defaultdict
import math

class VSM:
    vocab = set()
    vectors = defaultdict(list)
    def __init__(self, documents):
        self.documents= [doc.lower() for  doc in documents]
        for sent in documents:
            for word in sent.split():
                self.vocab.add(word.lower())
        self.vocab = sorted(self.vocab)
        # print(self.vocab)
    
    def make_vectors(self, query):
        vector = []
        for word in self.vocab:
                if word in query.lower().split():
                    vector.append(1)
                else:
                    vector.append(0)
        return vector
    
    def vectorize(self):
        for indx, doc in enumerate(self.documents):
            self.vectors[indx] = self.make_vectors(doc)
        # print(self.vectors)

    def cosine_similarity(self, v1, v2):
        numerator = 0
        d1 = 0
        d2 = 0
        for i in range(len(v1)):
            numerator += v1[i] * v2[i]
            d1 += v1[i] * v1[i]
            d2 += v2[i] * v2[i]
        return numerator/math.sqrt(d1 * d2)

    def find_similar(self, query):
        query_vector = self.make_vectors(query)
        scores = []
        for indx in range(len(self.documents)):
            scores.append(self.cosine_similarity(self.vectors[indx], query_vector))
        return scores


vsm = VSM([
    'the quick brown fox jumps over the lazy dog',
    'a fast agile fox leaped across a sleeping canine',
    'dogs are loyal pets and they sleep a lot',
    'foxes are cunning animals that often appear in folklore'
    ])
vsm.vectorize()
scores = vsm.find_similar('fox sleeping')
print('Scores: ')
for i in range(len(scores)):
    print(vsm.documents[i], ': ' ,scores[i])
