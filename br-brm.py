from collections import defaultdict

class BooleanRetrieval:
    vocab = set()
    incidence_matrix = defaultdict(list)

    def __init__(self, documents):
        self.documents = [doc.lower() for doc in documents]
        for doc in self.documents:
            for word in doc.split():
                self.vocab.add(word)
        self.vocab = sorted(self.vocab)

    def build_incidence_matrix(self):
        for word in self.vocab:
            self.incidence_matrix[word] = []
            for doc in self.documents:
                if word in doc.split():
                    self.incidence_matrix[word].append(1)
                else:
                    self.incidence_matrix[word].append(0)

    def boolean_and(self, query):
        terms = [term.lower() for term in query.split(" AND ")]
        if not terms or any(term not in self.incidence_matrix for term in terms):
            return [0] * len(self.documents)

        result = self.incidence_matrix[terms[0]]
        for term in terms[1:]:
            result = [a & b for a, b in zip(result, self.incidence_matrix[term])]
        return result

    def retrieve(self, query):
        result = self.boolean_and(query)
        matching_docs = []
        for idx, val in enumerate(result):
            if val == 1:
                matching_docs.append(self.documents[idx])
        return matching_docs


br = BooleanRetrieval([
    'the quick brown fox jumps over the lazy dog',
    'a fast agile fox leaped across a sleeping canine',
    'dogs are loyal pets and they sleep a lot',
    'foxes are cunning animals that often appear in folklore'
])
br.build_incidence_matrix()

results = br.retrieve('fox AND dog')
print('Matching Documents for query "fox AND dog":')
for doc in results:
    print(doc)
