def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_counts = {}
    for char in text:
        char_case = char.lower()
        if char_case in char_counts:
            char_counts[char_case] = char_counts[char_case] + 1
        else:
            char_counts[char_case] = 1
    return char_counts

def sort_on(item):
    return item["num"]

def sort_char_counts(counts):
    sorted_list = []
    for char, num in counts.items():
        pair = {"char": char, "num": num}
        sorted_list.append(pair)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list