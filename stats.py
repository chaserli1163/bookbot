def word_counter(string):
    number_of_words = len(string.split())
    return number_of_words


def char_counter(string):
    result = {}
    for char in string:
        char = char.lower()
        if char not in result:
            result[char] = 1
        else:
            result[char] += 1
    return result


def dic_sorter(dic):
    sorted_list_of_dic = []
    for i in dic:
        if i.isalpha():
            sorted_list_of_dic.append({"char": i, "num": dic[i]})
            sorted_list_of_dic.sort(reverse=True, key=get_num)
    return sorted_list_of_dic


def get_num(g):
    return g["num"]
