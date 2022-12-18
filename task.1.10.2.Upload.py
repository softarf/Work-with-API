# -*- coding: utf-8 -*-
#                        Задача №2. Сохранить указанный файл на Яндекс.Диске.
#
import os
import requests


def input_file_name():
    return input()


def input_token():
    my_token = input()
    return my_token


class YaUploader:

    def __init__(self, token: str):
        self.token = token

    def choose_data_straem(self, file_name: str):
        """Метод определяет источник данных для отправки на Я.Диск"""
        self.data_straem = open(file_name, 'rb')

    def get_href(self, file_path: str):
        """Метод получает ссылку для загрузки данных"""
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"  # из документации по Я.Диск
        my_params = {"path": file_path, "overwrite": "true"}
        my_headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}
        self.href = requests.get(url=upload_url, params=my_params, headers=my_headers).json().get("href", "")

    def upload_file(self) -> str:
        """Метод отправляет файл на Яндекс Диск"""
        my_response = requests.put(url=self.href, data=self.data_straem)
        # Функция может ничего не возвращать (из лекции)
        if 200 <= my_response.status_code < 300:
            return "'Success'"  # "Успешно"
        return "'Что-то не так: Status Code " + str(my_response.status_code) + "'"  # "Ошибка"

def main():
    # Получает путь к загружаемому файлу и токен от пользователя: test_05-15.txt
    my_file = input_file_name()
    TOKEN = input_token()
    uploader = YaUploader(TOKEN)
    uploader.choose_data_straem(my_file)
    path_to_file = 'disk:/' + os.path.basename(my_file)
    uploader.get_href(path_to_file)
    res = uploader.upload_file()
    print(res)


if __name__ == '__main__':
    main()


print('\n  -- Конец --  ')  # - Для блокнота
# input('\n  -- Конец --  ')	#	Типа  "Пауза" - Для среды
