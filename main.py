import sys
from stats import sort_character_dict
from stats import count_words
from stats import count_characters


def get_book_text(bookpath):
    with open(bookpath) as f:   
        return f.read()


def get_book_path(arg_list):
    if len(arg_list) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    return arg_list[1]


def main():
    bookpath = get_book_path(sys.argv)
    book_string = get_book_text(bookpath)
    num_words = count_words(book_string)
    character_dict = count_characters(book_string)
    sorted_list = sort_character_dict(character_dict)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookpath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")


main()

