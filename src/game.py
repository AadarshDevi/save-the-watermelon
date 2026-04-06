
from src.logic import GameLogic
from src.words import WordLoader


def main_game_loop():
    wl: WordLoader = WordLoader()
    wl.read_words("../data/words.txt")

    slices = 6
    gl: GameLogic = GameLogic(slices, wl.get_new_word())

    running: bool = True
    restart_game: bool = False
    printGameInfo: bool = True

    while running:

        if restart_game:
            print("Game Restarted")
            gl.reset_game_logic(slices)
            gl.set_new_word(wl.get_new_word())
            restart_game = False
            printGameInfo: bool = True
            if 3 <= len(gl.get_visual_word()) < 6:
                gl.get_hint()
            elif 6 <= len(gl.get_visual_word()) < 10:
                gl.get_hint()
                gl.get_hint()
            elif 10 <= len(gl.get_visual_word()):
                gl.get_hint()
                gl.get_hint()
                gl.get_hint()
            print_slices(gl.get_slices())
            print_options()
            print("Word:", " ".join(gl.get_visual_word()))

        user_input: str = input("Guess a letter: ").lower()

        if user_input == "":
            print("Please enter a letter")
            continue

        if user_input.startswith("-"):
            match user_input:
                case "-e":
                    restart_game = False
                    running = False
                    printGameInfo: bool = True
                case "-n":
                    restart_game = True
            continue

        valid_input: list = gl.valid_user_input(user_input)
        if not valid_input[0]:
            print(valid_input[1])
            printGameInfo = False
            pass

        isValidLetter: list = gl.check_letter(user_input)
        print(isValidLetter[1])
        printGameInfo = True

        if not gl.check_game_over():
            continue

        if gl.get_slices() == 0:
            print("\nPlayer was unable to save the watermelon")
        elif gl.visual_letter_count_reached():
            print("Player saved the watermelon")
        print("The word was", "".join(gl.get_visual_word()))

        running = False

        newRound: str = input("\nDo you want to play another round (Y/n)? ")
        if newRound.lower().startswith("y"):
            running = True
            restart_game = True

    print("\nThank you for playing Save the Watermelon")

    pass

def print_slices(slices: int):
    print("     ∧      " * slices)
    print("    / \\     " * slices)
    print("   /  0\\    " * slices)
    print("  /0    \\   " * slices)
    print(" /  0 0  \\  " * slices)
    print("|_________| " * slices)
    print("|_________| " * slices)
    pass

def print_options():
    print("\nGame Options:", end=" ")
    print("[-e]", "Exit Game", end="  ")
    # print("[-h]", "Letter Hint", end="  ")
    print("[-n]", "New Game")
    pass


main_game_loop()