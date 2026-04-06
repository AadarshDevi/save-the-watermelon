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

    def reset_game_logic(self, slices):
        self.__slices: int = slices
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
        if self.visual_letter_count_reached():
            return [False, "No hints can be given because the word is already found"]

        hintAttempt: int = 1
        maxHintAttempt: int = 5

        validHint: bool = False
        while not validHint:

            if hintAttempt > maxHintAttempt:
                break

            randomInt: int = random.randint(0, len(self.__word) - 1)

            if self.__visual_word[randomInt] == "__":
                self.check_letter(self.__word[randomInt])
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
        else:
            self.__letters_entered.append(letter)

        letterFound: bool = False

        for index in range(0, len(self.__word)):
            char = self.__word[index]
            if char != letter:
                continue

            self.__visual_word[index] = self.__word[index]
            self.__visible_letters += 1
            # self.debug_print()
            letterFound = True

        if not letterFound:
            self.__slices -= 1
            # self.debug_print()
            return [False, "ERROR > letter not found"]

        # self.debug_print()
        return [True, "INFO > The letter is in the word"]

    def check_game_over(self):
        if self.__slices == 0 or self.visual_letter_count_reached():
            return True
        return False

    def valid_user_input(self, userInput: str):
        if userInput == "" or len(userInput) > 1 or not userInput.isalpha():
            return [False, "ERROR > Please enter a letter"]
        return [True, "INFO > Player has entered valid input"]

    def get_visual_word(self):
        return self.__visual_word

    def get_visual_letter_count(self):
        return self.__visible_letters

    def visual_letter_count_reached(self):
        return self.__visible_letters == len(self.__word)

    def debug_print(self):

        print(self.__visual_word)
        print(self.__word)
        print(self.__visible_letters)
        print(self.__letters_entered)
        print(self.__slices)
