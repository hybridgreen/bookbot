# Imports
from stats import *
from sys import *

#Functions defs
def get_book_text(book_path):
    with open(book_path) as book:
       return book.read()
    
#Defining main
def main():
    try:
        file_path = argv[1]
        book_text = get_book_text(file_path)
        num_words = word_count(book_text)
        o_char_count = order_char_count(get_char_count(book_text))
        print(f"============ BOOKBOT ============ \n Analyzing book found at books/frankenstein.txt... \n ----------- Word Count ---------- \n Found {num_words} total words \n --------- Character Count -------" )
        for item in o_char_count:
            if item["char"].isalpha():
                print(str(item["char"]) + ": " + str(item["num"]))
        print("============= END ===============")

    
    except IndexError:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    except Exception as e:
        print(e)
        
#Running
main()