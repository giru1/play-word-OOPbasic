from os.path import isfile

import requests


def load_json(url):
    """
    Функция получает json для дальнейщей работы
    :param url: url- адрес, для получения json
    :return: json
    """
    response = requests.get(url)
    if response.status_code == 200:
        response_json = response.json()
        return response_json
    else:
        print('Sever return status code not 200')
        return False


def load_answer_words(path):
    """
    Ф-ия для создания списка существующих слов
    :param path: Получает путь к файлу
    :return: список правильных(существующтх) слов
    """
    answer_words = []
    if isfile(path):
        with open(path, 'r', encoding="utf-8") as f:
            for word in f:
                answer_words.append(word.strip('\n'))
    else:
        print(f'{path} not found')

    return answer_words
