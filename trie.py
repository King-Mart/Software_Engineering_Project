class Trie_cell():
    #A Trie is a tree where its elements are organized by their characters
    def __init__(self) -> None:
        #here im veryfing that if the current sequence is a word or not
        self.is_end_of_word = False
        #Here I give the max lenght that can be made with the prefix
        self.max_length = 0
        #map?
        self.map : dict[str, Trie_cell] = {}
        #letter associated with this cell will be last character of prefix
        self.prefix = ""
        #indent number so its easier to print
        self.indent_number = 0
        #

    def __repr__(self) -> str:
        return "\n" + "    "*self.indent_number + f"{self.indent_number}th letter. The prefix {self.prefix} is {'a word' if self.is_end_of_word else 'not a word'} the longest word that stems from this prefix is {self.max_length} characters long\n{str(self.map.values()).replace('dict_values([', '').replace('])', '')}"
        
    def show(self):
        print(self.map)

class Trie():
    def __init__(self, root : Trie_cell = Trie_cell(), initial_list : list[str] = []) -> None:
        self.root = root
        if initial_list:
            self.insert_list(initial_list)
        self.alphabet = ['a','b','c','d','e','f,','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    def __repr__(self) -> str:
        return str(self.root.map)
    
    def insert(self, word : str):
    # A function where well insert new words

        temp = self.root
        self.root.max_length = len(word)
        for i in range(len(word)):    # for each character of the word, we'll add them as prefixes to the map
            x = word[i]  # x is the current character
            
            # if there is no path to this, then make a new node
            if x not in temp.map:
                temp.map[x] = Trie_cell()
                temp.map[x].prefix = word[:i+1]
            temp.map[x].max_length = max(len(word), temp.map[x].max_length)
            temp.map[x].indent_number =  i+1

            temp = temp.map[x]

        temp.is_end_of_word = True
    def insert_list(self, list_of_word : list[str]):
        for word in list_of_word:
            self.insert(word)
        
    def search(self, word : str) -> list[str]:
        """
        missing_letter word takes a word with missing letters in this format wo?d and returns a list of all the possible words that it could be, eg. : wood, word, etc.

        :param word: it is the word with ? written for the unkown letters
        :param available_letters: is the parameter for inputing the allowed letters (like in wordle for example) if empty, it will use all letters

        :return: It returns list of all the possible words where all the letters but the ? match and are of the same lenght
        """
        return_list = []
        #A list with all the possible prefixes
        to_iterate : list[Trie_cell] = []
        to_show = []
        temp : Trie_cell = self.root
        if word[0] in temp.map:
            linked_cell = temp.map[word[0]]
            if linked_cell.max_length >= len(word):
                if linked_cell.prefix.__len__() == word.__len__() and linked_cell.is_end_of_word:
                    return_list.append(linked_cell.prefix)
                #If we are not on the last letter:
                else:
                    to_iterate.append(linked_cell)
                    to_show.append(linked_cell.prefix)

        # if len(word) > 1:
        for i in range(1, len(word)):
            x = word[i]
            new_iterate = []
            new_show = []
            for cell in to_iterate:
                if x in cell.map:
                    linked_cell = cell.map[x]
                    if linked_cell.max_length >= len(word):
                        if linked_cell.prefix.__len__() == word.__len__() and linked_cell.is_end_of_word:
                            return_list.append(linked_cell.prefix)
                        #If we are not on the last letter:
                        elif len(word)-1 > i:
                            new_iterate.append(linked_cell)
                            new_show.append(linked_cell.prefix)
            to_iterate, to_show = new_iterate, new_show

        #     to_iterate = list(x.prefix for x in temp.map.values() if x.max_lenght >= len(word))
        # for i in range(len(word)):
        #     x = word[i]
        return return_list
    
    def missing_letter_word(self, word : str) -> list[str]:
        """
        missing_letter word takes a word with missing letters in this format wo?d and returns a list of all the possible words that it could be, eg. : wood, word, etc.

        :param word: it is the word with ? written for the unkown letters
        :param available_letters: is the parameter for inputing the allowed letters (like in wordle for example) if empty, it will use all letters

        :return: It returns list of all the possible words where all the letters but the ? match and are of the same lenght
        """
        return_list = []
        #A list with all the possible prefixes
        to_iterate : list[Trie_cell] = []
        to_show = []
        temp : Trie_cell = self.root
        if word[0] == "?":
            #first verify if we start  with many letters or only one
            for linked_cell in temp.map.values():
                #Only carry on with branches who can have words that long
                if linked_cell.max_length >= len(word):
                    #if we already found working words then append them to the result list
                    if linked_cell.prefix.__len__() == word.__len__() and linked_cell.is_end_of_word:
                        return_list.append(linked_cell.prefix)
                    #If the word isnt one character, then prepare the iteration list to search for the next characters
                    elif len(word) > 1:
                        to_iterate.append(linked_cell)
                        to_show.append(linked_cell.prefix)
        else:
            if word[0] in temp.map:
                linked_cell = temp.map[word[0]]
                if linked_cell.max_length >= len(word):
                    if linked_cell.prefix.__len__() == word.__len__() and linked_cell.is_end_of_word:
                        return_list.append(linked_cell.prefix)
                    #If we are not on the last letter:
                    else:
                        to_iterate.append(linked_cell)
                        to_show.append(linked_cell.prefix)

        # if len(word) > 1:
        for i in range(1, len(word)):
            x = word[i]
            new_iterate = []
            new_show = []
            if x == "?":
                for cell in to_iterate:
                    for linked_cell in cell.map.values():
                        #Only carry on with branches who can have words that long
                        if linked_cell.max_length >= len(word):
                            #if we already found working words then append them to the result list
                            if linked_cell.prefix.__len__() == word.__len__() and linked_cell.is_end_of_word:
                                return_list.append(linked_cell.prefix)
                            #If we are not on the last letter:
                            elif len(word)-1 > i:
                                new_iterate.append(linked_cell)
                                new_show.append(linked_cell.prefix)
                to_iterate, to_show = new_iterate, new_show
            else:
                for cell in to_iterate:
                    if x in cell.map:
                        linked_cell = cell.map[x]
                        if linked_cell.max_length >= len(word):
                            if linked_cell.prefix.__len__() == word.__len__() and linked_cell.is_end_of_word:
                                return_list.append(linked_cell.prefix)
                            #If we are not on the last letter:
                            elif len(word)-1 > i:
                                new_iterate.append(linked_cell)
                                new_show.append(linked_cell.prefix)
                to_iterate, to_show = new_iterate, new_show

        #     to_iterate = list(x.prefix for x in temp.map.values() if x.max_lenght >= len(word))
        # for i in range(len(word)):
        #     x = word[i]
        return return_list
    def missing_letter_word_set_letters(self, word : str, available_letters : list =  ['a','b','c','d','e','f,','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']) -> list[str]:
        """
        missing_letter word takes a word with missing letters in this format wo?d and returns a list of all the possible words that it could be, eg. : wood, word, etc.

        :param word: it is the word with ? written for the unkown letters
        :param available_letters: is the parameter for inputing the allowed letters (like in wordle for example) if empty, it will use all letters
        :param list: is the list of letters available to make your word. by default all letters are allowed

        :return: It returns list of all the possible words where all the letters but the ? match and are of the same lenght
        """
        return_list = []
        #A list with all the possible prefixes
        to_iterate : list[Trie_cell] = []
        to_show = []
        temp : Trie_cell = self.root
        if word[0] == "?":
            #first check the first cell to give a list of possibilities to the other cells
            for linked_cell in temp.map.values():
                if linked_cell.prefix[-1] in available_letters:
                    #Only carry on with branches who can have words that long
                    if linked_cell.max_length >= len(word):
                        #if we already found working words then append them to the result list
                        if linked_cell.prefix.__len__() == word.__len__() and linked_cell.is_end_of_word:
                            return_list.append(linked_cell.prefix)
                        #If the word isnt one character, then prepare the iteration list to search for the next characters
                        elif len(word) > 1:
                            to_iterate.append(linked_cell)
                            to_show.append(linked_cell.prefix)
        else:
            if word[0] in temp.map:
                linked_cell = temp.map[word[0]]
                if linked_cell.max_length >= len(word):
                    if linked_cell.prefix.__len__() == word.__len__() and linked_cell.is_end_of_word:
                        return_list.append(linked_cell.prefix)
                    #If we are not on the last letter:
                    else:
                        to_iterate.append(linked_cell)
                        to_show.append(linked_cell.prefix)

        # if len(word) > 1:
        for i in range(1, len(word)):
            x = word[i]
            new_iterate = []
            new_show = []
            if x == "?":
                for cell in to_iterate:
                    for linked_cell in cell.map.values():
                        #Only take allowed lettrs for unkowns
                        if linked_cell.prefix[-1] in available_letters:
                            #Only carry on with branches who can have words that long
                            if linked_cell.max_length >= len(word):
                                #if we already found working words then append them to the result list
                                if linked_cell.prefix.__len__() == word.__len__() and linked_cell.is_end_of_word:
                                    return_list.append(linked_cell.prefix)
                                #If we are not on the last letter:
                                elif len(word)-1 > i:
                                    new_iterate.append(linked_cell)
                                    new_show.append(linked_cell.prefix)
                to_iterate, to_show = new_iterate, new_show
            else:
                for cell in to_iterate:
                    if x in cell.map:
                        linked_cell = cell.map[x]
                        if linked_cell.max_length >= len(word):
                            if linked_cell.prefix.__len__() == word.__len__() and linked_cell.is_end_of_word:
                                return_list.append(linked_cell.prefix)
                            #If we are not on the last letter:
                            elif len(word)-1 > i:
                                new_iterate.append(linked_cell)
                                new_show.append(linked_cell.prefix)
                to_iterate, to_show = new_iterate, new_show

        #     to_iterate = list(x.prefix for x in temp.map.values() if x.max_lenght >= len(word))
        # for i in range(len(word)):
        #     x = word[i]
        return return_list
    def missing_letter_word_must_letters(self, word : str, must_letters : list =  []) -> list[str]:
        """
        missing_letter word takes a word with missing letters in this format wo?d and returns a list of all the possible words that it could be, eg. : wood, word, etc.

        :param word: it is the word with ? written for the unkown letters
        :param available_letters: is the parameter for inputing the allowed letters (like in wordle for example) if empty, it will use all letters
        :param list: is the list of letters available to make your word. by default all letters are allowed

        :return: It returns list of all the possible words where all the letters but the ? match and are of the same lenght
        """
        return_list = []
        #A list with all the possible prefixes
        to_iterate : list[Trie_cell] = []
        to_show = []
        temp : Trie_cell = self.root
        if word[0] == "?":
            #first check the first cell to give a list of possibilities to the other cells
            for linked_cell in temp.map.values():
                #Only carry on with branches who can have words that long
                if linked_cell.max_length >= len(word):
                    #if we already found working words then append them to the result list
                    if linked_cell.prefix.__len__() == word.__len__() and linked_cell.is_end_of_word:
                        if all(letter in linked_cell.prefix for letter in must_letters) : return_list.append(linked_cell.prefix)
                    #If the word isnt one character, then prepare the iteration list to search for the next characters
                    elif len(word) > 1:
                        to_iterate.append(linked_cell)
                        to_show.append(linked_cell.prefix)
        else:
            if word[0] in temp.map:
                linked_cell = temp.map[word[0]]
                if linked_cell.max_length >= len(word):
                    if linked_cell.prefix.__len__() == word.__len__() and linked_cell.is_end_of_word:
                        return_list.append(linked_cell.prefix)
                    #If we are not on the last letter:
                    else:
                        to_iterate.append(linked_cell)
                        to_show.append(linked_cell.prefix)

        # if len(word) > 1:
        for i in range(1, len(word)):
            x = word[i]
            new_iterate = []
            new_show = []
            if x == "?":
                for cell in to_iterate:
                    for linked_cell in cell.map.values():
                        #Only carry on with branches who can have words that long
                        if linked_cell.max_length >= len(word):
                            #if we already found working words then append them to the result list
                            if linked_cell.prefix.__len__() == word.__len__() and linked_cell.is_end_of_word:
                                if all(letter in linked_cell.prefix for letter in must_letters) : return_list.append(linked_cell.prefix)
                            #If we are not on the last letter:
                            elif len(word)-1 > i:
                                new_iterate.append(linked_cell)
                                new_show.append(linked_cell.prefix)
                to_iterate, to_show = new_iterate, new_show
            else:
                for cell in to_iterate:
                    if x in cell.map:
                        linked_cell = cell.map[x]
                        if linked_cell.max_length >= len(word):
                            if linked_cell.prefix.__len__() == word.__len__() and linked_cell.is_end_of_word:
                                if all(letter in linked_cell.prefix for letter in must_letters)  : return_list.append(linked_cell.prefix)
                            #If we are not on the last letter:
                            elif len(word)-1 > i:
                                new_iterate.append(linked_cell)
                                new_show.append(linked_cell.prefix)
                to_iterate, to_show = new_iterate, new_show

        #     to_iterate = list(x.prefix for x in temp.map.values() if x.max_lenght >= len(word))
        # for i in range(len(word)):
        #     x = word[i]
        return return_list
    def missing_letter_word_not_letters(self, word : str, must_letters : list =  []) -> list[str]:
        """
        missing_letter word takes a word with missing letters in this format wo?d and returns a list of all the possible words that it could be, eg. : wood, word, etc.

        :param word: it is the word with ? written for the unkown letters
        :param available_letters: is the parameter for inputing the allowed letters (like in wordle for example) if empty, it will use all letters
        :param list: is the list of letters available to make your word. by default all letters are allowed

        :return: It returns list of all the possible words where all the letters but the ? match and are of the same lenght
        """
        return_list = []
        #A list with all the possible prefixes
        to_iterate : list[Trie_cell] = []
        to_show = []
        temp : Trie_cell = self.root
        if word[0] == "?":
            #first check the first cell to give a list of possibilities to the other cells
            for linked_cell in temp.map.values():
                #Only carry on with branches who can have words that long
                if linked_cell.max_length >= len(word):
                    #if we already found working words then append them to the result list
                    if linked_cell.prefix.__len__() == word.__len__() and linked_cell.is_end_of_word:
                        if all(letter not in linked_cell.prefix for letter in must_letters) : return_list.append(linked_cell.prefix)
                    #If the word isnt one character, then prepare the iteration list to search for the next characters
                    elif len(word) > 1:
                        to_iterate.append(linked_cell)
                        to_show.append(linked_cell.prefix)
        else:
            if word[0] in temp.map:
                linked_cell = temp.map[word[0]]
                if linked_cell.max_length >= len(word):
                    if linked_cell.prefix.__len__() == word.__len__() and linked_cell.is_end_of_word:
                        return_list.append(linked_cell.prefix)
                    #If we are not on the last letter:
                    else:
                        to_iterate.append(linked_cell)
                        to_show.append(linked_cell.prefix)

        # if len(word) > 1:
        for i in range(1, len(word)):
            x = word[i]
            new_iterate = []
            new_show = []
            if x == "?":
                for cell in to_iterate:
                    for linked_cell in cell.map.values():
                        #Only carry on with branches who can have words that long
                        if linked_cell.max_length >= len(word):
                            #if we already found working words then append them to the result list
                            if linked_cell.prefix.__len__() == word.__len__() and linked_cell.is_end_of_word:
                                if all(letter not in linked_cell.prefix for letter in must_letters) : return_list.append(linked_cell.prefix)
                            elif len(word)-1 > i:
                                new_iterate.append(linked_cell)
                                new_show.append(linked_cell.prefix)
                to_iterate, to_show = new_iterate, new_show
            else:
                for cell in to_iterate:
                    if x in cell.map:
                        linked_cell = cell.map[x]
                        if linked_cell.max_length >= len(word):
                            if linked_cell.prefix.__len__() == word.__len__() and linked_cell.is_end_of_word:
                                if all(letter not in linked_cell.prefix or letter in word for letter in must_letters)  : return_list.append(linked_cell.prefix)
                                # else:
                                #     print(linked_cell.prefix, must_letters)
                            #If we are not on the last letter:
                            elif len(word)-1 > i:
                                new_iterate.append(linked_cell)
                                new_show.append(linked_cell.prefix)
                to_iterate, to_show = new_iterate, new_show

        #     to_iterate = list(x.prefix for x in temp.map.values() if x.max_lenght >= len(word))
        # for i in range(len(word)):
        #     x = word[i]
        return return_list
    #TANGLE FUNCTION IS BROKEN AND DOES NOT WORK, IT SHOULD NOT BE USED
    def tangle(self, initial, target):
        #TODO, RETURN THE PATH TO THE SOLUTION
        turn = 0
        curr_lookup :list = [initial]
        next_lookup :list = []
        lookup_origin = {}
        paths : dict[str, str] = {}
        while True:
            temp_look = []
            for lookup in curr_lookup:
                neighbors = get_neighbours(lookup)
                temp_look += neighbors
                for neighbor in neighbors:
                    if neighbor in lookup_origin:
                        print(f"Conflict, {neighbor} comes from {lookup} and {lookup_origin[neighbor]}")
                    lookup_origin[neighbor] = lookup
            
            curr_lookup = temp_look
            for lookup in list(set(curr_lookup)):
                next_moves = self.missing_letter_word(lookup)
                next_lookup += next_moves

                for move in next_moves:
                    if move in paths:
                        print(f"Conflict, {move} comes from {lookup_origin[lookup]} and {paths[move]}")
                    paths[move] = lookup_origin[lookup]
            next_lookup = list(set(next_lookup))
            if target in next_lookup:
                print(get_path_to_end(target, initial, paths))
                break

            turn += 1
            curr_lookup = next_lookup
            next_lookup = []
            if turn == 8: break
            
def get_neighbours(word):
    next_lookup = []
    for i in range(len(word)):
        next_lookup.append(word[:i] + "?" + word[i+1:])
    return next_lookup
def get_path_to_end(end, beginning, dictionary):
    path = [end]
    turn = 0
    while True:
        path.append(dictionary[path[-1]])
        turn += 1
        if turn == 10: break

    return path.reverse()