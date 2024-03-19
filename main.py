def main():
    book_path = "books/frankenstein.txt"
    book = get_book(book_path)

    word_count = count_words(book)
    character_count = sort_characters(count_characters(book))

    print_report(book_path, word_count, character_count)

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

def sort_characters(characters):
    return dict(sorted(characters.items(), key=lambda pair: pair[1], reverse=True))

def print_report(book_path, word_count, character_count):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()

    for character, total in character_count.items():
        print(f"The '{character}' character was found {total} times")

    print("--- End report ---")

main()
