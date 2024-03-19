def main():
    book_path = "books/frankenstein.txt"
    book = get_book(book_path)
    print(book)

def get_book(path):
    with open(path) as book:
        return book.read()

main()
