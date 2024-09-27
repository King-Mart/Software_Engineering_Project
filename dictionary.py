import Trie.trie as trie

dictionary = open("english3.txt", encoding="utf8").read().splitlines()

dictionary = trie.Trie(trie.Trie_cell(),dictionary)
while True:
    choice = input("Tangle (t) or uknown letters (ul)?\n").replace(" ", "").lower()
    if choice == "ul":
        lookup = input("Write the word you want to lookup, write ? for each missing letters, write nothing to exit, if you wanna set specific letters to use, add them after a / (wo?d/wdr) : \n").replace(" ", "").lower().split("/")
        if len(lookup) == 2:
            print("Here are all the possibilities with the letters")
            print(dictionary.missing_letter_word_must_letters(lookup[0], list(lookup[1])))
            print("And without them")
            print(dictionary.missing_letter_word_not_letters(lookup[0], list(lookup[1])))
        if lookup[0] == "":
            break
        else:
            print("Here are all the possibilities")
            print(lookup)
            print(dictionary.missing_letter_word(lookup ))
    elif choice == "t" or "tangle":
        initial = input("Initial word : \n").replace(" ", "")
        final = input("Final word : \n").replace(" ", "")
        dictionary.tangle(initial, final)
