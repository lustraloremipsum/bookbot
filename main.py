def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"\n{get_number_of_words(text)} words found in the document")
    
    character_count = count_characters(text)
    character_count_list = []
    for character in character_count:
        if character.isalpha():
            character_count_list.append({"name":character, "num":character_count[character]})
    character_count_list.sort(reverse=True, key=sort_on)
    print("")
    for character in character_count_list:
        print(f"The {character['name']} was found {character['num']} times")   

def sort_on(dict):
    return dict['num']


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_number_of_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    # Make a set out of the text to loop through
    text_set = set(text.lower())
    character_count = {}

    for character in text_set:
        character_count[character] = text.count(character)
    
    return character_count


if __name__ == "__main__":
    main()