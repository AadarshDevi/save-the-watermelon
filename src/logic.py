import random


class GameLogic:
    """The GameLogic class holds all the decision-making for the game like in valid user input, and showing the letters guessed on the terminal"""

    def __init__(self, slices, word):
        """Initializes the game logic with the needed variables made private to not accidentally change it"""
        self.__slices: int = slices
        self.__word: list = list(word)
        self.__visual_word: list = ["__"] * len(self.__word)
        self.__visible_letters: int = 0
        self.__letters_entered: list = []

        # self.debug_print()
        pass

    def reset_game_logic(self, slices):
        """Resets the game by resetting the slices, word, the word seen on the terminal (visual word) and other important vars"""
        self.__slices: int = slices
        self.__word: list = []
        self.__visual_word: list = []
        self.__visible_letters: int = 0
        self.__letters_entered: list = []

        # self.debug_print()
        pass

    def set_new_word(self, word):
        """Setting a new word to guess and updating the visual word"""
        self.__word: list = list(word)
        self.__visual_word: list = ["__"] * len(self.__word)
        pass

    def get_slices(self):
        """getter for the slices"""
        return self.__slices

    def get_hint(self):
        """Gives the user a hint by unveiling a letter"""

        # check if all letters are not visible
        if self.visual_letter_count_reached():
            return [False, "No hints can be given because the word is already found"]

        # loop vars to stop infinite loops
        hintAttempt: int = 1
        maxHintAttempt: int = 5

        # getting a hint that is valid aka no hint or not duplicating a hint
        validHint: bool = False
        while not validHint:

            # break of infinite loop
            if hintAttempt > maxHintAttempt:
                break

            # random index to reveal random letter of the word
            randomInt: int = random.randint(0, len(self.__word) - 1)

            if self.__visual_word[randomInt] == "__":
                self.check_letter(self.__word[randomInt])
                validHint = True
                continue

            hintAttempt += 1

        # telling the user if the hint was not successfully shown
        if not validHint:
            return [False, "Unable to give a hint"]

        return [True, "Hint has been given"]

    def check_letter(self, letter: str):
        """Checks if the letter is in the word"""

        # letter already entered by user
        if letter in self.__letters_entered:
            return [False, "letter has already been entered"]
        else:
            self.__letters_entered.append(letter)

        letterFound: bool = False

        # showing the letter if it is in the word
        for index in range(0, len(self.__word)):
            char = self.__word[index]
            if char != letter:
                continue

            self.__visual_word[index] = self.__word[index]
            self.__visible_letters += 1
            # self.debug_print()
            letterFound = True

        # letter is not found in the word
        if not letterFound:
            self.__slices -= 1
            # self.debug_print()
            return [False, "The letter is not in the word"]

        # self.debug_print()
        return [True, "The letter is in the word"]

    def check_game_over(self):
        """checks if the game is over. the game is over when the slices are a 0 or all the letters are unveiled"""
        if self.__slices == 0 or self.visual_letter_count_reached():
            return True
        return False

    def valid_user_input(self, userInput: str):
        """checks if the user's input is valid but it not being empty, not equal to 1 or is not an alphabet """
        if userInput == "" or not len(userInput) == 1 or not userInput.isalpha():
            return [False, "Please enter a letter, not a number or a symbol"]
        return [True, "Player has entered valid input"]

    def get_visual_word(self):
        """getter for the visual word (the word seen by the user)"""
        return self.__visual_word

    def get_visual_letter_count(self):
        """gets the letters that have been inputted by the user. used for debugging"""
        return self.__visible_letters

    def visual_letter_count_reached(self):
        """checks if the all the letters have been unveiled"""
        return self.__visible_letters == len(self.__word)

    def debug_print(self):
        """printing the variables to see their values realtime and is mainly for debugging and will not be seen in the terminal when playing"""
        print(self.__visual_word)
        print(self.__word)
        print(self.__visible_letters)
        print(self.__letters_entered)
        print(self.__slices)

    def get_secret_word(self):
        """return the word the player was guessing"""
        return self.__word