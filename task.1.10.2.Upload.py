# -*- coding: utf-8 -*-
#                        Задача №2. Сохранить указанный файл на Яндекс.Диске.
#
from typing import BinaryIO, Optional

import os
import requests


def input_file_name() -> str:
    return input()


def input_token() -> str:
    my_token: str = input()
    # или можно считать из файла ...
    return my_token


class YaUploader:

    def __init__(self, token: str) -> None:
        self.token: str = token
        self.data_stream: Optional[BinaryIO] = None
        self.href: str = ''

    def choose_data_stream(self, file_name: str) -> None:
        """Метод определяет источник данных для отправки на Я.Диск"""
        self.data_stream = open(file_name, 'rb')

    def get_href(self, file_path: str) -> None:
        """Метод получает ссылку для загрузки данных"""
        upload_url: str = 'https://cloud-api.yandex.net/v1/disk/resources/upload'  # из документации по Я.Диск
        my_params: dict = {'path': file_path, 'overwrite': 'true'}
        my_headers: dict = {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}
        self.href = requests.get(url=upload_url, params=my_params, headers=my_headers).json().get("href", "")

    def upload_file(self) -> str:
        """Метод отправляет файл на Яндекс Диск"""
        my_response = requests.put(url=self.href, data=self.data_stream)
        # Функция может ничего не возвращать (из лекции)
        if 200 <= my_response.status_code < 300:
            return "'Success'"  # "Успешно"
        return f"'Что-то не так: Status Code {my_response.status_code}'"  # "Ошибка"


def main() -> None:
    # Получает от пользователя путь к загружаемому файлу (test_05-15.txt) и токен.
    my_file: str = input_file_name()
    TOKEN: str = input_token()
    uploader = YaUploader(TOKEN)
    uploader.choose_data_stream(my_file)
    path_to_file: str = 'disk:/' + os.path.basename(my_file)
    uploader.get_href(path_to_file)
    res: str = uploader.upload_file()
    print(res)


if __name__ == '__main__':
    main()
    # input('\n  -- Конец --  ')    #	Типа  "Пауза" - Для среды
    # print('\n  -- Конец --  ')  # - Для блокнота
