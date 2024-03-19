'''
Создайте класс студента.
○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв. Если ФИО не соответствует условию, выведите:


ФИО должно состоять только из букв и начинаться с заглавной буквы
○ Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы. Если такого предмета нет, выведите:


Предмет {Название предмета} не найден
○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100). В противном случае выведите:


Оценка должна быть целым числом от 2 до 5

Результат теста должен быть целым числом от 0 до 100
○ Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.

Вам предоставлен файл subjects.csv, содержащий предметы. Сейчас в файл записана следующая информация.


Математика,Физика,История,Литература
Создайте класс Student, который будет представлять студента и его успехи по предметам. Класс должен иметь следующие методы:
Атрибуты класса:

name (str): ФИО студента. subjects (dict): Словарь, который хранит предметы в качестве ключей и информацию об оценках и результатах тестов для каждого предмета в виде словаря.

Магические методы (Dunder-методы):

__init__(self, name, subjects_file): Конструктор класса. Принимает имя студента и файл с предметами и их результатами. Инициализирует атрибуты name и subjects и вызывает метод load_subjects для загрузки предметов из файла.

__setattr__(self, name, value): Дескриптор, который проверяет установку атрибута name. Убеждается, что name начинается с заглавной буквы и состоит только из букв.

__getattr__(self, name): Позволяет получать значения атрибутов предметов (оценок и результатов тестов) по их именам.

__str__(self): Возвращает строковое представление студента, включая имя и список предметов.
Студент: Иван Иванов
Предметы: Математика, История

Методы класса:

load_subjects(self, subjects_file): Загружает предметы из файла CSV. Использует модуль csv для чтения данных из файла и добавляет предметы в атрибут subjects.

add_grade(self, subject, grade): Добавляет оценку по заданному предмету. Убеждается, что оценка является целым числом от 2 до 5.

add_test_score(self, subject, test_score): Добавляет результат теста по заданному предмету. Убеждается, что результат теста является целым числом от 0 до 100.

get_average_test_score(self, subject): Возвращает средний балл по тестам для заданного предмета.

get_average_grade(self): Возвращает средний балл по всем предметам.
'''

import csv


class NameValidator:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not all(map(lambda val: val.istitle(), value.split(' '))):
            raise ValueError(f"ФИО должно начинаться с заглавной буквы!")
        instance.__dict__[self.name] = value


class Student:
    name = NameValidator()

    def __init__(self, name):
        self.name = name
        self.subject_grades = {}
        self.subject_tests = {}

        with open('PycharmProjects\pythonProjectGB\Seminar_12\subject.py', 'r') as csv_file:
            subject = csv.reader(csv_file, delimiter="\n")
            for item in subject:
                self.subject_grades[item[0]] = []
                self.subject_tests[item[0]] = []

    def add_score(self, score, subject):
        if score < 2 or score > 5:
            raise ValueError("Оценка должна быть от 2 до 5")
        self.subject_grades[subject].append(score)

    def add_test_result(self, result, subject):
        if result < 0 or result > 100:
            raise ValueError("Результат теста должен быть от 0 до 100")
        self.subject_tests[subject].append(result)

    def average_score_student(self):
        subject_scores = [sum(score) for score in self.subject_grades.values() if score != []]
        if not subject_scores:
            return 0
        return sum(subject_scores) / len(subject_scores)

    def subject_test_average(self, subject):
        return subject, sum(self.subject_tests[subject]) / len(self.subject_tests[subject])




