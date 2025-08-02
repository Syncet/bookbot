def get_word_count(book):
    words = book.split()
    word_count = len(words)
    return word_count
def get_char(word):
    letters = {}
    for letter in word.lower():
        if letter not in letters:
            letters[letter] = 1
        elif letter in letters:
            letters[letter] += 1
    update = sort(letters)
    return update
    
def sort(letters):
    sorted_char = []       
    for list_char, count in letters.items():
        new_dic = {"char": list_char, "num": count}
        sorted_char.append(new_dic) 
    sorted_char.sort(reverse=True, key=lambda item: item["num"])
    return sorted_char
