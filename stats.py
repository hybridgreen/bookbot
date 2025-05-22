from string import ascii_lowercase

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict["num"]


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

def order_char_count(count):
    ordered = []
    for item in count:
        ordered.append({"char":item , "num": count[item]})
    ordered.sort(reverse=True,key = sort_on )
    return ordered
