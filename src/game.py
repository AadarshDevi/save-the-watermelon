
from src.logic import GameLogic
from src.words import WordLoader


def main_game_loop():
    """This is the main game loop for Save the Watermelon and will control the game logic and getting words"""

    # create word loader and get list of words from a word file
    wl: WordLoader = WordLoader()
    wl.read_words("../data/words.txt")

    # setting up lives, initializing GameLogic object, and booleans to run the game
    slices = 6
    gl: GameLogic = GameLogic(slices, wl.get_new_word())

    running: bool = True
    restart_game: bool = False
    printGameInfo: bool = True

    # the while loop that will run the game
    while running:

        # reset game when player wants to guess a new word
        if restart_game:
            print("Game Restarted")
            gl.reset_game_logic(slices)
            gl.set_new_word(wl.get_new_word())
            restart_game = False
            printGameInfo: bool = True

            # hints for the words is based on the length of the word
            if 3 <= len(gl.get_visual_word()) < 6:
                gl.get_hint()
            elif 6 <= len(gl.get_visual_word()) < 10:
                gl.get_hint()
                gl.get_hint()
            elif 10 <= len(gl.get_visual_word()):
                gl.get_hint()
                gl.get_hint()
                gl.get_hint()

        # print the slices, game options, and the word as blank spacs with letters filled
        if printGameInfo:
            print_slices(gl.get_slices())
            print_options()
            print("Word:", " ".join(gl.get_visual_word()))

        # user input
        user_input: str = input("Guess a letter: ").lower()

        # check if input is empty
        if user_input == "":
            print("Please enter a letter")
            continue

        # checking if input is a game option
        if user_input.startswith("-"):
            match user_input:
                case "-e":
                    restart_game = False
                    running = False
                    printGameInfo: bool = True
                case "-n":
                    restart_game = True
            continue

        # checking if input given is a letter
        valid_input: list = gl.valid_user_input(user_input)
        if not valid_input[0]:
            print(valid_input[1])
            printGameInfo = False
            pass

        # using the letter to guess if it is in the word
        isValidLetter: list = gl.check_letter(user_input)
        print(isValidLetter[1])
        printGameInfo = True

        # checking if game not over
        if not gl.check_game_over():
            continue

        # checking if player has won the game or not and printing the word
        if gl.get_slices() == 0:
            print("\nPlayer was unable to save the watermelon")
        elif gl.visual_letter_count_reached():
            print("Player saved the watermelon")
        print("The word was", "".join(gl.get_visual_word()))

        # game is not running
        running = False

        # does player want to guess a new word
        newRound: str = input("\nDo you want to play another round (Y/n)? ")
        if newRound.lower().startswith("y"):
            running = True
            restart_game = True

    # telling the player thanks for playing the game
    print("\nThank you for playing Save the Watermelon")


def print_slices(slices: int):
    """prints the slices (lives) the player has and the slice is represented using ASCII art"""
    print("     ∧      " * slices)
    print("    / \\     " * slices)
    print("   /  0\\    " * slices)
    print("  /0    \\   " * slices)
    print(" /  0 0  \\  " * slices)
    print("|_________| " * slices)
    print("|_________| " * slices)
    pass

def print_options():
    """prints the options of the game. separated from the game loop so adding more option text will be easier"""
    print("\nGame Options:", end=" ")
    print("[-e]", "Exit Game", end="  ")
    # print("[-h]", "Letter Hint", end="  ") # code exists but logic was buggy
    print("[-n]", "New Game")
    pass

# call the start of the game
main_game_loop()