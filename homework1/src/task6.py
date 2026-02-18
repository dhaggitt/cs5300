from pathlib import Path

# Counts the number of words in a text file
def count_words(filename):
    word_count = 0
    try:
        with filename.open() as file:
            content = file.read()
            words = content.split()
            word_count = len(words)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    return word_count

# Main declared for debugging
def main():
    filename = "task6_read_me.txt"
    filepath = Path.cwd() / filename
    print(count_words(filepath)) 

if __name__ == "__main__":
    main()