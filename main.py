def get_book_text(book_path):
    with open(book_path) as book:
       return book.read()

def main():
    try:
        #book_text = get_book_text(input("Please enter the books file path:"))
        book_text = get_book_text("books/frankenstein.txt")
        #print(book_text)
        num_words = word_count(book_text)
        print(f"{num_words} words found in the document")
    except Exception as e:
        print(e)

main()