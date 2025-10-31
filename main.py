from stats import *
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
        return file_content


def main(f):
    input_string = get_book_text(f)
    number_of_words = word_counter(input_string)
    sorted_list = dic_sorter(char_counter(input_string))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {f}...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")
    for i in sorted_list:
        print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")


if len(sys.argv)<2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main(sys.argv[1])

#main()

#"books/frankenstein.txt"