
def term_frequency(filename):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read().lower()
    words = text.split()
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    print("Term Frequency:")
    for word, count in freq.items():
        print(word, ":", count)

file = "sample.txt"
term_frequency(file)
