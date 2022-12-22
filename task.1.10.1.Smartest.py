# -*- coding: utf-8 -*-
#                        Задача №1.  Кто самый умный "супергерой"?
#
from typing import Tuple, List, Any

import requests


def input_data() -> Tuple[List[str], Any]:
    inspect_heroes: List[str] = ['Hulk', 'Captain America', 'Thanos']
    my_url: str = 'https://akabab.github.io/superhero-api/api/all.json'
    my_response: Any = requests.get(url=my_url)
    return inspect_heroes, my_response.json()


def collate_heroes(inspect_heroes: List[str], all_heroes: Any) -> Tuple[str, int]:
    max_intelligence: int = 0
    superhero_name: str = ""
    temp_list: List[str] = inspect_heroes[:]
    for item in all_heroes:
        if len(temp_list) > 0:

            #     1. Реализация через конструкцию try-except.
            #     2. Реализация через дополнительный вложенный цикл по списку сравниваемых "героев".
            #     3. Ещё одна реализация с пользовательской функцией find_in_list().

            #     4. Реализацию через проверку вхождения в список считаю наиболее понятной.
            if item['name'] in temp_list:
                if item['powerstats']['intelligence'] > max_intelligence:
                    max_intelligence = item['powerstats']['intelligence']
                    superhero_name = item['name']
                temp_list.remove(item['name'])
        else:
            break
    return superhero_name, max_intelligence


def output_res(inspect_heroes: List[str], hero: str, intelligence: int) -> None:
    print(' Кто самый умный среди "супергероев":', *inspect_heroes, end='')
    print('?')
    if intelligence > 0:
        print(f' Это {hero}, его интелект = {intelligence}')
    else:
        print(' Таких нет в этой Галактике.')


def main() -> None:
    #                  1. Принимает исходные данные.
    inspect_heroes, all_heroes = input_data()
    #                  2. Решает задачу.
    hero, intelligence = collate_heroes(inspect_heroes, all_heroes)
    #                  3. Выводит ответ.
    output_res(inspect_heroes, hero, intelligence)


if __name__ == '__main__':
    main()
    # input('\n  -- Конец --  ')	#	Типа  "Пауза" - Для среды
    # print('\n  -- Конец --  ')  # - Для блокнота
