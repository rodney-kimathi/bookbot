def main():
    book_path = "books/frankenstein.txt"
    book = get_book(book_path)

    word_count = count_words(book)
    print("Number of words:", word_count)

def get_book(path):
    with open(path) as book:
        return book.read()
    
def count_words(text):
    return len(text.split())

main()
