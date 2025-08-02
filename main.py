from stats import get_word_count
from stats import get_char
import sys
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    imported_book = sys.argv[1]
def get_book_text(book):
    with open(book) as f:
        file_contents = f.read()
    
    return file_contents 
    

def main():
    book = imported_book
    words = get_book_text(book)
    counted_words = get_word_count(words)
    letters = get_char(words)
    print("============ BOOKBOT ============")
    print("Analyzing book found at " + book)
    print("----------- Word Count ----------")
    print("Found " + str(counted_words) + " total words")
    print("--------- Character Count -------")
    for i in letters:
        if i["char"].isalpha():
            print(i["char"] + ": " + str(i["num"]))
    print("============= END ===============")

main()