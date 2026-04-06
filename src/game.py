
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
def print_slices(slices: int):
    print("     ∧      " * slices)
    print("    / \\     " * slices)
    print("   /  0\\    " * slices)
    print("  /0    \\   " * slices)
    print(" /  0 0  \\  " * slices)
    print("|_________| " * slices)
    print("|_________| " * slices)
    pass
