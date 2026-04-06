import random


class GameLogic:

    def __init__(self, slices, word):
        self.__slices: int = slices
        self.__word: list = list(word)
        self.__visual_word: list = ["__"] * len(self.__word)
        self.__visible_letters: int = 0
        self.__letters_entered: list = []

        # self.debug_print()
        pass

    def reset_game_logic(self):
        self.__slices: int = 6
        self.__word: list = []
        self.__visual_word: list = []
        self.__visible_letters: int = 0
        self.__letters_entered: list = []

        # self.debug_print()
        pass

    def set_new_word(self, word):
        self.__word: list = list(word)
        self.__visual_word: list = ["__"] * len(self.__word)
        pass

    def get_slices(self):
        return self.__slices

    def get_hint(self):
        if self.__visible_letters == 0:
            return [False, "No hints can be given because the word is already found"]

        hintAttempt: int = 1
        maxHintAttempt: int = 5

        validHint: bool = False
        while not validHint:

            if hintAttempt > maxHintAttempt:
                break

            randomInt: int = random.randint(0, len(self.__word) - 1)
            if self.__visual_word[randomInt] == "_":
                self.__visual_word[randomInt] = self.__word[randomInt]

            if self.__visual_word[randomInt] == "__":
                # self.__visual_word[randomInt] = self.__word[randomInt]
                # self.debug_print()
                # self.__visible_letters += 1
                validHint = True
                continue

            hintAttempt += 1

        if not validHint:
            return [False, "Unable to give a hint"]

        return [True, "Hint has been given"]

    def check_letter(self, letter: str):

        if letter in self.__letters_entered:
            return [False, "letter has already been entered"]

        letterFound: bool = False

        for index in range(0, len(self.__word)):
            char = self.__word[index]
            if char != letter:
                continue

            self.__visual_word[index] = self.__word[index]
            self.__visible_letters += 1

            if letter not in self.__letters_entered:
                self.__letters_entered.append(letter)
                letterFound = True
            # self.debug_print()

        if not letterFound:
            return [False, "letter not found"]
            # self.debug_print()

        return [True, "letter has been found"]
        # self.debug_print()

    def check_game_over(self):
        if self.__visible_letters == len(self.__word):
            return False
        return True




    def valid_user_input(self, input: str):
        if len(input) != 1:
            return [False, "Player must enter a letter"]

    def debug_print(self):

        print(self.__visual_word)
        print(self.__word)
        print(self.__visible_letters)
        print(self.__letters_entered)
        print(self.__slices)
