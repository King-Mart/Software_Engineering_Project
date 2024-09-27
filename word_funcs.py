import trie
word_list =  ["apple", "banana", "plane", "cow", "moon", "man", "app", "martial", "art", "skill", "elixir", "strenght", "muscle", "bee", "code", "computer", "comply", "compile", "hungry", "zebra", "soldier", 'a', 'i']

            

        



root = trie.Trie_cell()
table = trie.Trie(root)
table.insert_list(word_list)

print(table.missing_letter_word("s?????h?"))
print(table.tangle("mango","lemon"))