
"""В организации есть два типа людей: сотрудники и обычные люди. Каждый человек (и сотрудник, и обычный) имеет следующие атрибуты:

Фамилия (строка, не пустая) Имя (строка, не пустая) Отчество (строка, не пустая) Возраст (целое положительное число) Сотрудники имеют также уникальный идентификационный номер (ID), который должен быть шестизначным положительным целым числом.

Ваша задача:

Создать класс Person, который будет иметь атрибуты и методы для управления данными о людях (Фамилия, Имя, Отчество, Возраст). Класс должен проверять валидность входных данных и генерировать исключения InvalidNameError и InvalidAgeError, если данные неверные.

Создать класс Employee, который будет наследовать класс Person и добавлять уникальный идентификационный номер (ID). Класс Employee также должен проверять валидность ID и генерировать исключение InvalidIdError, если ID неверный.

Добавить метод birthday в класс Person, который будет увеличивать возраст человека на 1 год.

Добавить метод get_level в класс Employee, который будет возвращать уровень сотрудника на основе суммы цифр в его ID (по остатку от деления на 7).

Создать несколько объектов класса Person и Employee с разными данными и проверить, что исключения работают корректно при передаче неверных данных.
"""
class Employee:
    #==========================================================================
    def __init__(self, surname, name, patronymic, position, employment_date, salary_level ):
        self._surname          = surname
        self._name             = name
        self._patronymic       = patronymic
        self.__position        = position
        self.__employment_date = employment_date
        self.__salary_level    = salary_level
    # ==========================================================================
    def __str__(self):
        return ( f'Сотрудник {self._surname} {self._name} {self._patronymic}\n'
               f'\tпринят на работу {self.__employment_date} на должность {self.__position} '
                 f'с окладом {self.__salary_level}' )
#==============================================================================
dir = Employee('Иванов', 'Иван', 'Иваныч', 'директор', '01.02.2000', 'дохрена!))')
dv  = Employee('Сидорчук', 'Сидор', 'Сидорыч', 'старший дворник', '11.11.2002', 'не ахти((')
mns = Employee('Башмачкин', 'Акакий', 'Акакиевич', 'младший научный сотрудник', '21.12.2022', 'так себе...')
print(dir)
print()
print(dv)
print()
print(mns)
print()
dir._name      = 'Петр'
dir.__position = 'конюх'
print(dir)