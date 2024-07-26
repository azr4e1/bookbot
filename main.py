import sys


def main():
    path = sys.argv[1]
    pprint(path)


def count_words(book):
    words = book.split()

    return len(words)


def count_chars(book):
    counter = {}
    for char in book:
        char_lower = char.lower()
        if char_lower not in counter:
            counter[char_lower] = 0
        counter[char_lower] += 1

    return counter


def get_text(path):
    with open("./books/frankenstein.txt") as f:
        return f.read()


def pprint(path):
    book = get_text(path)
    words = count_words(book)
    chars = count_chars(book)
    ascending_order_chars = sorted(
        list(chars.keys()), key=lambda x: chars[x], reverse=True)

    print(f"--- Begin report of {path} ---")
    print(f"{words} found in the document\n")
    for char in ascending_order_chars:
        if char.isalpha():
            count = chars[char]
            print(f"The '{char}' character was found {count} times")
    print("--- End report ---")


main()
