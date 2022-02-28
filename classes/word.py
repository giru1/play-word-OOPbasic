class Word:

    def __init__(self, word):
        self.word = word

    def __repr__(self):
        return self.word

    def is_contain(self, sub_word):
        """
        Функция проверки составлении слова из букв
        :param sub_word: Слово введенное пользователем
        :return: Boolean
        """
        main_word = self.word
        for letter in sub_word:
            if letter not in main_word:
                return False
            else:
                main_word = main_word.replace(letter, '', 1)
        return True
