import trie
import pathlib

#Get the directory where the file is located
path = str(pathlib.Path(__file__).parent.resolve())

#d_path is a variable that contains the location of the dictionaries to load Trie\Dictionaries\english3.txt
d_path = path + "/Dictionaries/"
dictionary = open(d_path +"english3.txt", encoding="utf8").read().splitlines()

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
            print(lookup[0] + " : ")
            print(dictionary.missing_letter_word(lookup[0]))
    elif choice == "t" or "tangle":
        initial = input("Initial word : \n").replace(" ", "")
        final = input("Final word : \n").replace(" ", "")
        dictionary.tangle(initial, final)
