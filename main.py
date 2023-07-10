bookpath = "./books/frankenstein.txt"


def count_words(text):
    results_dict = {}
    for char in "abcdefghijklmnopqrstuvwxyz":
        char_occurrences = text.lower().count(char)
        results_dict[char] = char_occurrences
    return results_dict


def create_report(filepath, word_count, char_dict):
    vals_list = list(char_dict.values())
    print(f"--- Begin report of {filepath} ---")
    print(f"{word_count} words were found in the document")
    for val in sorted(vals_list, reverse=True):
        print(
            f"The '{list(char_dict.keys())[vals_list.index(val)]}' character was found {val} times"
        )
    print("--- End report ---")


with open(bookpath) as f:
    text = f.read()
    num_words = len(text.split())
    letter_count = count_words(text)
    create_report(bookpath, num_words, letter_count)
