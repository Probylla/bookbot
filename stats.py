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
    return (f"{text_len} words found in the document")
#takes file and counts words
def stats():
    letter_count = {}
    book_text = get_book_text("books/frankenstein.txt")
    book_text = book_text.lower()
    for letter in book_text:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return (letter_count)
#counts letters in text

def sort_on(items):
    return items["num"]

def sort_dict():
    sorted_dict = []
    letter_count = {}
    letter_count = stats()

    for letter in letter_count:
        if letter.isalpha() == True:
            sorted_dict.append(
                {"name": letter, "num": letter_count[letter]} 
            ) 
    sorted_dict.sort(reverse= True,key=sort_on)
    return sorted_dict
#sorts dict

def generate_report():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(main())
    print("--------- Character Count -------")
    sorted_dict = sort_dict()
    for letter in sorted_dict:
        print(f"{letter["name"]}: {letter["num"]}")
    print("============= END ===============")
#prints report
