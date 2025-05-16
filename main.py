import sys
from stats import get_counts_sorted, get_num_words, get_character_counts

# BOOK="books/frankenstein.txt"

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        BOOK=sys.argv[1]
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {BOOK}...")
        with open(BOOK, encoding='utf-8-sig') as f:
            book_content = f.read()
            print("----------- Word Count ----------")
            print(f"Found {get_num_words(book_content)} total words")
            print("--------- Character Count -------")
            for line in get_counts_sorted(get_character_counts(book_content)):
                print(f"{line["char"]}: {line["count"]}")
            print("============= END ===============")

main()
