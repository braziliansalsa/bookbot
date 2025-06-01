
def main():
    path_to_file = "books/frankenstein.txt"
    book_text = get_book_text(path_to_file)
    num_words = count_words(book_text)
    print(f"{num_words} words found in the document")
def get_book_text(path_to_file):
    
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def count_words(file_contents):
    words = file_contents.split()
    return len(words)

main()