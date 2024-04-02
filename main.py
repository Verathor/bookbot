def main():
    bookpath = "books/frankenstein.txt"

def return_wordcount():
    with open(bookpath, "r") as file:
        data = file.read()
        words = data.split()
        wordcount = len(words)
    return wordcount

main()

