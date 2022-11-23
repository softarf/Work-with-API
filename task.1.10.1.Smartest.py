# -*- coding: utf-8 -*-
#                        Задача №1.  Кто самый умный "супергерой"?
#
import requests


def input_data():
    inspect_heros = ['Hulk', 'Captain America', 'Thanos']
    my_url = 'https://akabab.github.io/superhero-api/api/all.json'
    my_response = requests.get(url=my_url)
    return inspect_heros, my_response.json()


def collate_heros(inspect_heros, all_heros):
    max_intelligence = 0
    superhero_name = ""
    temp_list = inspect_heros[:]
    for item in all_heros:
        if len(temp_list) > 0:

            #     Реализация через конструкцию try-except.
            try:
                i = temp_list.index(item['name'])    # К сожалению, у списков нет метода .find()
            except ValueError:
                pass    # Пропускает этого "супергероя", т.к. его нет среди интересующих нас.
            else:
                if item['powerstats']['intelligence'] > max_intelligence:
                    max_intelligence= item['powerstats']['intelligence']
                    superhero_name = temp_list[i]
                temp_list.pop(i)

            # #     Реализация без конструкции try-except.
            # for elem in temp_list:
            #     if elem == item['name']:
            #         if item['powerstats']['intelligence'] > max_intelligence:
            #             max_intelligence= item['powerstats']['intelligence']
            #             superhero_name = elem
            #         temp_list.remove(elem)
            #         break

        else:
            break
    return superhero_name, max_intelligence


def output_res(inspect_heros, hero, intelligence):
    print(' Кто самый умный среди "супергероев":', *inspect_heros, end='')
    print('?')
    if intelligence > 0:
        print(f' Это {hero}, его интелект = {intelligence}')
    else:
        print(' Таких нет в этой Галактике.')


if __name__ == '__main__':
    #                  1. Подготавливает исходные данные.
    inspect_heros, all_heros = input_data()
    #                  2. Решает задачу.
    hero, intelligence = collate_heros(inspect_heros, all_heros)
    #                  3. Выводит ответ.
    output_res(inspect_heros, hero, intelligence)

print('\n  -- Конец --  ')    #                 - Для блокнота
# input('\n  -- Конец --  ')	#	Типа  "Пауза" - Для среды
