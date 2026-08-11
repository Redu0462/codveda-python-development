def count_words(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        words = content.split()
        return len(words)
    except FileNotFoundError:
        return "File not found!"

filename = input("Enter the filename: ")
result = count_words(filename)
print(result)
    