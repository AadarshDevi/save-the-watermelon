import random


class GameLogic:
    def __init__(self, slices, word):
        self.__slices: int = slices
        self.__word: list = list(word)
        self.__visual_word: list = ["_"] * len(self.__word)
        self.__visible_letters: int = 0
        self.__letters_entered: list = []
        pass

    def reset_game_logic(self):
        self.__slices: int = 6
        self.__word: list = []
        self.__visual_word: list = []
        self.__visible_letters: int = 0
        self.__letters_entered: list = []
        pass

    def set_new_word(self, word):
        self.__word: list = list(word)
        self.__visual_word: list = ["_"] * len(self.__word)
        pass



    def check_game_over(self):
        if self.__visible_letters == len(self.__word):
            return False
        return True

    def valid_user_input(self, input: str):
        if len(input) != 1:
            return [False, "Player must enter a letter"]

        if not input.isalpha():
            return [False, "Player must enter a letter"]

        return [True, "Player has entered valid input"]