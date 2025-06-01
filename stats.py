def count_words(file_contents):
    words = file_contents.split()
    return len(words)

def count_characters(file_contents):
    characters = file_contents.lower()
    dict_characters = {}
    for char in characters:
        dict_characters[char] = dict_characters.get(char, 0) + 1
    return dict_characters
