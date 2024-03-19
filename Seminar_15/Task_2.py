"""
 Возьмите любые 1-3 задачи из прошлых домашних заданий. Добавьте к ним логирование ошибок и полезной информации.
 Также реализуйте возможность запуска из командной строки с передачей параметров.
"""

import argparse
from collections import Counter
import logging
from typing import List

# Настройка логирования
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def find_duplicates(numbers: List[int]) -> List[int]:
    """Функция для поиска дубликатов в списке."""
    # Используем Counter для подсчета повторяющихся элементов
    counter = Counter(numbers)
    # Список дубликатов - элементы, которые встречаются более одного раза
    duplicates = [item for item, count in counter.items() if count > 1]
    return duplicates


def main(numbers: List[int]):
    """Основная функция для обработки и вывода результата."""
    logging.info(f"Processing list: {numbers}")
    # Ищем дубликаты в списке
    result = find_duplicates(numbers)
    # Выводим результат
    print(f'Duplicates: {result}')
    # Записываем результат в лог
    logging.info(f'Duplicates: {result}')


if __name__ == '__main__':
    # Парсинг аргументов командной строки
    parser = argparse.ArgumentParser(
        description='Find duplicates in a list of integers.')
    parser.add_argument('-l', '--list', nargs='+', type=int,
                        help='List of integers to process.')
    args = parser.parse_args()

    if args.list:
        # Если передан список в аргументах, используем его
        main(args.list)
    else:
        # Иначе используем список по умолчанию
        default_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5, 4, 3, 2, 1]
        main(default_list)