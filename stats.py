def get_book_text (filepath):
    with open(filepath) as book:
        book_text = book.read()
        return book_text
#opens file and reads it as string
def main(filepath):
    word_list = []
    book_text = get_book_text(filepath)
    word_list = book_text.split()
    text_len = len(word_list)
    return (f"Found {text_len} total words")
#takes file and counts words
def stats(filepath):
    letter_count = {}
    book_text = get_book_text(filepath)
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

def sort_dict(filepath):
    sorted_dict = []
    letter_count = {}
    letter_count = stats(filepath)

    for letter in letter_count:
        if letter.isalpha() == True:
            sorted_dict.append(
                {"name": letter, "num": letter_count[letter]} 
            ) 
    sorted_dict.sort(reverse= True,key=sort_on)
    return sorted_dict
#sorts dict

def generate_report(filepath):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(main(filepath))
    print("--------- Character Count -------")
    sorted_dict = sort_dict(filepath)
    for letter in sorted_dict:
        print(f"{letter["name"]}: {letter["num"]}")
    print("============= END ===============")
#prints report
