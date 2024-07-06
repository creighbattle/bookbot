def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_count_dict = count_characters(text)
    create_report(char_count_dict, text)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_word_count(text):
    words = text.split()
    return len(words)

def count_characters(text):

    char_count_dict = {}

    for char in text:
        char_lower = char.lower()
        if char_lower not in char_count_dict:
            char_count_dict[char_lower] = 1
        else:
            char_count_dict[char_lower] += 1

    return char_count_dict

def create_report(char_count_dict, text):
    word_count = get_word_count(text)
    char_count_list = char_count_dict.items()
    sorted_list = sorted(char_count_list, key=lambda char: char[1], reverse=True)
    print(sorted_list)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")

    for el in sorted_list:
        char = el[0]
        is_letter = char.isalpha()
        if is_letter:
            print(f"The '{char}' character was found {el[1]} times")

    print("--- End report ---")



main()