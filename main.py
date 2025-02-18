def main():
    path_to_file = "books/frankenstein.txt"
    alphabet = ['a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    with open(path_to_file) as f:
        file_contents = f.read()
    number_of_words = count_words(file_contents)
    number_of_chars_dict = aggregate_characters(file_contents)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f'{number_of_words} words found in the document\n')
    for key in number_of_chars_dict:
        if key in alphabet:
            print("The '{}' character was found {} times".format(key, number_of_chars_dict[key]))
    print("--- End report ---")

def count_words(file_string):
    return len(file_string.split())

def aggregate_characters(file_string):
    chars_dict = {} #initialize empty dict
    lower_case_file = file_string.lower() #put all chrs into lower case
    for char in lower_case_file:
        if char not in chars_dict:
            chars_dict[char] = 1
        else:
            chars_dict[char] += 1
    return chars_dict



main()