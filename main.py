from stats import *

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


main("books/frankenstein.txt")
#input_string = get_book_text("books/frankenstein.txt")
#dic = char_counter(input_string)
#list = dic_sorter(dic)
#print(list)
