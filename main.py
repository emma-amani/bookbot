from stats import word_count
from stats import char_count
from stats import sort_text
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path_to_book = sys.argv[1] 

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    text = get_book_text(sys.argv[1])
    num_words = word_count(text)
    num_char = char_count(text)
    print(f"Found {num_words} total words")
    sorted_chars = sort_text(num_char)
    for entry in sorted_chars:
        print(f"{entry['char']}: {entry['num']}")

main()

