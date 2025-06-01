from stats import count_words, count_characters, sorted_characters
import sys



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_file = sys.argv[1]
    book_text = get_book_text(path_to_file)
    num_words = count_words(book_text)
    dict_characters = count_characters(book_text)
    sorted_dict_list = sorted_characters(dict_characters)
    #print(f"{num_words} words found in the document")
    #print(f"{dict_characters} characters found in the document")
    report(path_to_file, num_words, sorted_dict_list)

def report(path_to_file, num_words, sorted_dict_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in sorted_dict_list:
        if char["char"].isalpha():
            print(f"{char['char']}: {char['num']}")
    print("============= END ===============")

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


main()