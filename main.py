def get_book_text(book):
    with open(book) as f:
        file_contents = f.read()
        get_word_count(file_contents)
    word_count = get_char(file_contents)
    print(word_count)
    return file_contents
from stats import get_word_count
from stats import get_char
def main():
    
    get_book_text("books/frankenstein.txt")
    
main()