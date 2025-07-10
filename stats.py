def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    dictionary = {}
    for char in text:
        char = char.lower()
        if char in dictionary:
            dictionary[char] = dictionary[char] + 1
        else:
            dictionary[char] = 1
    return dictionary

def sort_on(item):
    return item["num"]

def sort_text(dictionary):
    sorted_list = []
    for char, count in dictionary.items():
        if char.isalpha():
            new_dict = {"char": char, "num": count}
            sorted_list.append(new_dict)

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

