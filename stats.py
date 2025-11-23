def sort_on(items):
    return items["num"]


def sort_character_dict(character_dict):
    character_list = []
    for l in character_dict:
        character_list.append({"char" : l, "num" : character_dict[l]})
    character_list.sort(reverse=True, key=sort_on)
    return character_list


def count_characters(book_string):
    character_dict = {}
    book_list = book_string.split()
    for word in book_list:
        for l in word:
            l = l.lower()
            if not l.isalpha():
                continue
            if l in character_dict.keys():
                character_dict[l] = character_dict[l] + 1
                continue
            character_dict[l] = 1
    return character_dict


def count_words(book_string):
    book_list = book_string.split()
    return len(book_list)
