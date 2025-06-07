from stats import get_number_of_words

def get_book_text(book):
    with open(book, "r", encoding="utf-8") as f:
        return f.read()

def main():
    text = get_book_text("books/frankenstein.txt")
    word_count = get_number_of_words(text)
    print(f"{text}")
    print(f"{word_count} words found in the document")

if __name__ == "__main__":
    main()
