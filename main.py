import sys
from stats import get_num_words, get_char_freq, get_sorted_char_freq

# Get the file contents from a given relative file path
def get_book_text(file_path):
    file_contents = ""
    with open(file_path) as f:
        file_contents = f.read()

    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_relative_path = sys.argv[1]
    contents = get_book_text(file_relative_path)
    num_words = get_num_words(contents)
    #print(f"{num_words} words found in the document")

    char_freq = get_char_freq(contents)
    #print(char_freq)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_relative_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    get_sorted_char_freq(char_freq)
    print("============= END ===============")



main()