import random


class GameLogic:
    def __init__(self, slices, word):
        self.__slices: int = slices
        self.__word: list = list(word)
        self.__visual_word: list = ["_"] * len(self.__word)
        self.__visible_letters: int = 0
        self.__letters_entered: list = []
        pass

    def set_new_word(self, word):
        self.__word: list = list(word)
        self.__visual_word: list = ["_"] * len(self.__word)
        pass


