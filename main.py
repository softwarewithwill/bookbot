#no / infront of books
path_to_file = "books/frankenstein.txt"

#with starts a block, so indent below
with open(path_to_file) as f:
    file_contents = f.read()
    words = file_contents.split()
    #print(len(words))
    dictionary_chars = {}
    for word in words:
        for char in word:
            char = char.lower()
            if char in dictionary_chars:
                dictionary_chars[char] += 1
            else: dictionary_chars[char] = 1
    #print(dictionary_chars)
    only_alpha = {k: v for k, v in dictionary_chars.items() if k.isalpha()}
    sorted_alpha = list(only_alpha.items())
    sorted_alpha.sort(key=lambda x: x[1], reverse=True)
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{len(words)} words found in the file")
    for item in sorted_alpha:
        print(f"The {item[0]} character was found {item[1]} times")
    print(f"--- End Report ---")





