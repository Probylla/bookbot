def get_book_text (filepath):
    with open(filepath) as book:
        book_text = book.read()
        return book_text
#opens file and reads it as string
def main():
    word_list = []
    book_text = get_book_text("books/frankenstein.txt")
    word_list = book_text.split()
    text_len = len(word_list)
    print(f"{text_len} words found in the document")
#takes file and counts words
