import random


class WordLoader:

    def __init__(self):
        self.__words_list: list = []

    def read_words(self, filepath: str):
        self.__words_list: list = []
        file = open(filepath, "r")
        for line in file:
            if line.strip():
                self.__words_list.append(line.strip())
                # print(line.strip())
        file.close()

    def get_new_word(self):
        random_index = random.randint(0, len(self.__words_list) - 1)
        word: str = self.__words_list[random_index]
        self.__words_list.remove(word)
        return word