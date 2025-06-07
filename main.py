from stats import get_number_of_words, get_number_of_characters, get_sorted_characters

def get_book_text(book):
    with open(book, "r", encoding="utf-8") as f:
        return f.read()

def main():
    text = get_book_text("books/frankenstein.txt")
    word_count = get_number_of_words(text)
    num_char = get_number_of_characters(text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")

    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")
    for item in get_sorted_characters(num_char):
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
        else:
            continue
    print("============= END ===============")

main()
