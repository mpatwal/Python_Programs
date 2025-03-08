
def count_word_occurrences(filename, word):
    try:
        with open(filename, "r") as file:
            content = file.read()

        words = content.lower().split()
        return words.count(word.lower())

    except FileNotFoundError:
        print("File not found!")
        return None


filename = input("Enter the filename: ")
word = input("Enter the word to count: ")


count = count_word_occurrences(filename, word)


if count is not None:
    print(f"The word '{word}' appears {count} times in '{filename}'.")
