def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    words = count_char(text)
    print(f"{num_words} words found in the document")
    sort_dic = sort_on(words)
    print_dict(sort_dic)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_char(text):
    dict_count ={}
    for char in text:
        if char.lower() in dict_count:
            dict_count[char.lower()] += 1
        elif char.isalpha():
            dict_count[char.lower()] = 1
    return dict_count

def sort_on(dict):
    sort_dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    return sort_dict
def print_dict(dict):
     for i in dict:
         print(f"The {i[0]} character was found {i[1]} times")   

main()
