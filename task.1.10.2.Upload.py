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

    def upload(self, file_path: str, file_name: str):
        """Метод загружает файл в папку file_path на яндекс диск"""
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"  # из документации
        my_params = {"path": file_path, "overwrite": "true"}
        my_headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}
        #  Получает ссылку для загрузки файла
        my_href = requests.get(upload_url, params=my_params, headers=my_headers).json().get("href", "")
        #  Добавляет файл на Яндекс Диск
        my_response = requests.put(my_href, data=open(file_name, 'rb'))
        # Функция может ничего не возвращать
        if 200 <= my_response.status_code < 300:
            print("'Success'")  # "Успешно"


if __name__ == '__main__':
    # Получает путь к загружаемому файлу и токен от пользователя: test_05-15.txt
    file_name = input_file_name()
    TOKEN = input_token()
    uploader = YaUploader(TOKEN)
    path_to_file = 'disk:/' + os.path.basename(file_name)
    uploader.upload(path_to_file, file_name)

print('\n  -- Конец --  ')  # - Для блокнота
# input('\n  -- Конец --  ')	#	Типа  "Пауза" - Для среды
