def read_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()
    words = text.split()
    print("File Content:\n", text)
    print("Total Words:", len(words))

file = "sample.txt"
read_file(file)
