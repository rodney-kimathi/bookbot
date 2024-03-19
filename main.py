from document import *

def main():
    document_path = "documents/frankenstein.txt"
    document = get_document(document_path)

    word_count = count_words(document)
    character_count = sort_characters(count_characters(document))

    print_report(document_path, word_count, character_count)

main()
