def get_book_text (filepath):
    with open(filepath) as book:
        book_text = book.read()
        return book_text
#opens file and reads it as string
def main():
    book_text = get_book_text("books/frankenstein.txt")
    print(book_text)
    

main()

    