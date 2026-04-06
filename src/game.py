
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
            print_slices(gl.get_slices())
            print_options()
            print("Word:", " ".join(gl.get_visual_word()))
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