
import string

stop_words = {"the", "is", "at", "on", "and", "a", "an", "to", "of", "in", "am"} 

def clean_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read().lower()
    # remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = [w for w in text.split() if w not in stop_words]
    print("Cleaned Words:", words)

file = "br.txt"
clean_file(file)
