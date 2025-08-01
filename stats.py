def get_word_count(book):
    words = book.split()
    word_count = len(words)
    print(str(word_count) + " words found in the document")
def get_char(word):
    letters = {}
    for letter in word.lower():
        if letter not in letters:
            letters[letter] = 1
        elif letter in letters:
            letters[letter] += 1
    return letters
