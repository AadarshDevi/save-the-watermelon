import os
import random

class WordLoader:
    """loads words from the file and gives a random letter from that file"""

    def __init__(self):
        """initialize the word loader with an empty private (obfuscated) list of words"""
        self.__words_list: list = []

    def read_words(self, filepath: str):
        """reads the words from the file. if the line contains characters other than alphabets, it will not be saved in the list of words"""
        self.__words_list: list = []

        print(filepath)

        file = None
        try:
            file = open(filepath, "r") # open file
        except FileNotFoundError:
            current_dir = os.path.dirname(os.path.abspath(__file__)) # get current abs filepath (from C/D drive)
            filepath = os.path.join(current_dir, "..", "data", "words.txt") # find the data/words.txt file
            print(filepath)
            file = open(filepath, "r")  # open file



        for line in file: # reading the file line by line and adding the lines that have only alphabets
            if line.strip() and line.strip().isalpha():
                self.__words_list.append(line.strip())
                # print(line.strip())
        file.close()

    def get_new_word(self):
        """
        A random words from the list of words is returned after it is removed from that list
        :returns: a random word from the list of words
        """
        random_index = random.randint(0, len(self.__words_list) - 1)
        word: str = self.__words_list[random_index]
        self.__words_list.remove(word)
        return word