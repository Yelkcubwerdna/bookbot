def main():
    with open(file_path) as f:
        file_contents = f.read()

        print(f"--- Begin report of {file_path} ---")
        print(f"{word_count(file_contents)} words found in the document")
        print()

        characters = character_count(file_contents)

        def sort_on(dict):
            return dict["num"]
        
        characters.sort(reverse=True, key=sort_on)

        for i in characters:
            if i["char"].isalpha():
                print(f"The '{i['char']}' character was found {i['num']} times")

        print("--- End report ---")

def word_count(string):
    words = string.split()

    number = len(words)

    return number

def character_count(string):
    lowered_string = string.lower()

    characters = {}

    for c in lowered_string:
        try:
            characters[c] += 1
        except:
            characters[c] = 1

    list = []

    for k in characters:
        dict = {"char": k, "num": characters[k]}
        list.append(dict)

    return list

file_path = "books/frankenstein.txt"

main()