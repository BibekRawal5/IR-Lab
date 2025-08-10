with open("br-input.txt", "r") as f:
    text = f.read()
words = text.split()
print(f"Word count in br-input.txt: {len(words)}")
