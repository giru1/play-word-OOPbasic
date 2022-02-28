import json
import random
from os.path import isfile

from classes.player import Player
from classes.word import Word
from utils import load_json, load_answer_words

ANSWER_WORDS = 'answer_words.txt'
JSON_URL = 'https://jsonkeeper.com/b/GS1O'
RESULT_JSON = 'result.json'


def create_users():
    """
    Создание пользователей
    :return:
    """
    user_name_1 = input('Введите имя 1 игрока ')
    user_name_2 = input('Введите имя 2 игрока ')

    player_1 = Player(user_name_1)
    player_2 = Player(user_name_2)
    players = [player_1, player_2]

    print(f'Программа: {player_1.name} vs {player_2.name}, игра начинается!')

    return players


def create_word():
    """
    Берет список слов и возвращает случайное слово
    :return: Выводит выбранное слово
    """
    words = load_json(JSON_URL)
    word_random = random.choice(words)
    word_select = Word(word_random)
    return word_select


def win_user(players):
    """
    функция определения победителя
    :param players: список объектов класса Player
    :return: Вывод победившего игрока
    """

    if players[0].scores == players[1].scores:
        print('Ничья!')

    winner = max(players[0], players[1], key=lambda p: p.scores)
    print(f'Победил игрок – {winner}')
    print(f'======')


def result(players):
    """
    функция вывода результата после завершения программы
    :param players: список объектов класса Player
    :return: вывод результата игры(статистика)
    """
    print(f'Игра окончена\n' f'======')
    for player in players:
        print(f'Игрок 1 {player.name} - {player.scores}\n')

    print(f'======')


def save_result(word_select, words, players):
    """
    сохранение результата в файл
    :param word_select: списое слов введеннных на протяжении всей игры
    :param words: слово которое было дано на игру
    :param players: список объектов класса Player
    :return:
    """
    data = {
        "users": {
            "1": players[0].name,
            "2": players[1].name
        },
        "word": word_select.word,
        "words": words
    }

    with open(RESULT_JSON, 'w', encoding="windows-1251") as f:
        json.dump(data, f, ensure_ascii=False)
        print(f'Данные записаны в файл')


def main():

    word_select = create_word()
    players = create_users()
    words_answer = load_answer_words(ANSWER_WORDS)  # Список существующих слов

    print('Добро пожаловать в игру!')
    user_input = ''  # Ввод пользователя
    all_word = []  # Список слов использованных в игре

    while user_input != "stop":

        for player in players:
            print(f'Ваше слово на эту игру: {word_select.word}')
            print(f'Ходит игрок {player.name}\n'
                  f'Введите слово')

            user_input = input()

            if user_input in all_word:  # Проверка на повторный ввод слова
                print(f'Такое слово уже существует!')
                continue

            if user_input == '':  # Проверка на ввод пустоты
                print(f'Пустой ввод')
                continue

            if user_input == "stop":
                break

            player.words.append(user_input)  # Добавление введенного слова игроку
            all_word += player.words  # Добавление введенного слова в список использованных слов

            if word_select.is_contain(user_input) and user_input in words_answer:
                player.scores += len(user_input)  # Начисление баллов
                print('Принято')
            else:
                print('Нет такого слова.')

    result(players)
    win_user(players)
    save_result(word_select, all_word, players)


if __name__ == '__main__':
    main()
