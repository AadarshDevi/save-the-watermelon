import random


class WordLoader:

    def __init__(self):
        self.__words_list: list = []

    close file
    give the words_in_file list


def get_new_word
    get a psuedo random int in range of 0 to length of __words_list
    get a word from __words_list at the index of the pseudo random int
    increment the __word_index
    if word is empty
    give None

    def get_new_word(self):
        random_index = random.randint(0, len(self.__words_list) - 1)
        word: str = self.__words_list[random_index]
        self.__words_list.remove(word)
        return word