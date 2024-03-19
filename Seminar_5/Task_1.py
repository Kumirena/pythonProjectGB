#Напишите функцию, которая принимает на вход строку —
#абсолютный путь до файла. Функция возвращает кортеж из трёх
#элементов: путь, имя файла, расширение файла.


import os


string = 'C:/Users/Ir_Shel/Desktop/file.txt'

def get_file_info(f_path: str) -> tuple:
    path, filename = os.path.split(f_path)
    name, extension = filename.split('.')
    return path, name, extension

print(f'Исходная строка: {string} \nКортеж из пути: {get_file_info(string)}')