def get_book_text(book):
    with open(book, "r", encoding="utf-8") as f:
        return print(f.read())
    return None

def main():
    text = get_book_text("books/frankenstein.txt")

main()
