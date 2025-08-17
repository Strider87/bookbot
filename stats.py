
# Get number of words from a given string
def get_num_words(file_contents):
    words = file_contents.split()
    return len(words)

# Get character frequency
def get_char_freq(file_contents):
    char_freq = {}
    for char in file_contents:
        if char != " ":
            lower_char = char.lower()
            if lower_char not in char_freq:
                char_freq[lower_char] = 1
            else:
                char_freq[lower_char] += 1
    
    return char_freq

# Report generation

def print_list(char_freq_list):
    for item in char_freq_list:
        print(f"{item["char"]}: {item["num"]}")

def sort_on(items):
    return items["num"]


def get_sorted_char_freq(char_freq):
    char_freq_list = []
    for key in char_freq:
        char_freq_list.append(
            {"char": key, "num": char_freq[key]}
        )
        
    char_freq_list.sort(reverse=True, key=sort_on)
    print_list(char_freq_list)
