def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    sorted_dict = []
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    chars_dict = get_chars_dict(text)
    sorted_dict = dict(sorted(chars_dict.items(), key=lambda x: x[1], reverse=True))
    for char, count in sorted_dict.items():
       print(f"The '{char}' character was found {count} times")
    print(f"--- End report ---")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_chars_dict(text):
    chars_dict = {}
    for char in text.lower():
        if char.isalpha():
            chars_dict[char] = chars_dict.get(char, 0) + 1
    return chars_dict

main()
