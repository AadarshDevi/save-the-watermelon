
from src.logic import GameLogic
from src.words import WordLoader


def main_game_loop():
    wl: WordLoader = WordLoader()
    wl.read_words("../data/words.txt")

    slices = 6
    wl: WordLoader = WordLoader
    gl: GameLogic = GameLogic()