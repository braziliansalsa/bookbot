def count_words(file_contents):
    words = file_contents.split()
    return len(words)

def count_characters(file_contents):
    characters = file_contents.lower()
    dict_characters = {}
    for char in characters:
        dict_characters[char] = dict_characters.get(char, 0) + 1
    return dict_characters

def sorted_characters(dict_characters):
    dict_list = []
    for char in dict_characters:
        new_dict = {"char": char, "num": dict_characters[char]}
        dict_list.append(new_dict)
    sorted_dict_list = sorted(dict_list, key=lambda item: item["num"], reverse=True)    
    return sorted_dict_list
    