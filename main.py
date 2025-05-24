import sys
if len(sys.argv) != 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)

from stats import get_num_words
from stats import count_characters
from stats import sort_char_counts


def get_book_text(path):
    with open(path) as f:
        contents = f.read()
    return contents

def main():
    book_text = get_book_text(sys.argv[1])
    char_counts = count_characters(book_text)
    num_words = get_num_words(book_text)
    print(f"Found {num_words} total words")
    #print(char_counts)
    
    sorted_chars = sort_char_counts(char_counts)
    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
        
main()