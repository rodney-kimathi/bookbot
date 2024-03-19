def main():
    book_path = "books/frankenstein.txt"
    book = get_book(book_path)

    word_count = count_words(book)
    print("Number of words:", word_count)

    character_count = count_characters(book)
    print("Number of characters:", character_count)

def get_book(path):
    with open(path) as book:
        return book.read()
    
def count_words(text):
    return len(text.split())

def count_characters(text):
    characters = {}

    for character in text:
        if not character.isalpha():
            continue

        character = character.lower()
        characters[character] = characters[character] + 1 if character in characters else 1

    return characters

main()
