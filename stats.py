def get_number_of_words(text):
    return len(text.split()) 

def get_number_of_characters(text):
    char_dict = {}
    for char in text:
        lowered = char.lower()
        if lowered in char_dict:
            char_dict[lowered] += 1
        else:
            char_dict[lowered] = 1
    return char_dict

def get_sorted_characters(dict_char):
    sorted_list = [{"char": num, "num": count} for num, count in dict_char.items()]
    sorted_list.sort(key=lambda item: item["num"], reverse=True)
    return sorted_list
