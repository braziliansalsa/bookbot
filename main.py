from stats import count_words, count_characters
def main():
    path_to_file = "books/frankenstein.txt"
    book_text = get_book_text(path_to_file)
    num_words = count_words(book_text)
    dict_characters = count_characters(book_text)
    print(f"{num_words} words found in the document")
    print(f"{dict_characters} characters found in the document")
    
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


main()