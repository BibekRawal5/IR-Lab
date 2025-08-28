from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

word = input("Enter a word: ").lower()
print("Stemmed Word:", stemmer.stem(word))
