from stats import get_word_count
from stats import get_char
import sys
print(sys.argv)
def get_book_text(book):
    with open(book) as f:
        file_contents = f.read()
    
    return file_contents 
    

def main():
    book = ""
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