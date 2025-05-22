from string import ascii_lowercase

def word_count(book):
    word_count = len(book.split())
    return word_count

def get_char_count(book):
    book = book.lower()
    char_count = {}
    for char in book:
        if char in char_count:
            char_count[char] +=1
        else:
            char_count[char] = 1
    return char_count
