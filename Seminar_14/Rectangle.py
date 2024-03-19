'''
Возьмите код из прошлой задачи "Класс Rectangle".

Напишите к ней тесты, используя unittest и лежать в class TestRectangle(unittest.TestCase)
'''
import warnings

warnings.filterwarnings('ignore')

# Введите ваше решение ниже
class Rectangle:
    """
    Класс, представляющий прямоугольник.

    Атрибуты:
    - width (int): ширина прямоугольника
    - height (int): высота прямоугольника

    Методы:
    - perimeter(): вычисляет периметр прямоугольника
    - area(): вычисляет площадь прямоугольника
    - __add__(other): определяет операцию сложения двух прямоугольников
    - __sub__(other): определяет операцию вычитания одного прямоугольника из другого
       - __lt__(other): определяет операцию "меньше" для двух прямоугольников
       - __eq__(other): определяет операцию "равно" для двух прямоугольников
       - __le__(other): определяет операцию "меньше или равно" для двух прямоугольников
       - __str__(): возвращает строковое представление прямоугольника
       - __repr__(): возвращает строковое представление прямоугольника, которое может быть использовано для создания нового объекта
       """

    def __init__(self, width, height=None):
        self.width = width
        if height is None:
            self.height = width
        else:
            self.height = height

    def perimeter(self):
        """
        Вычисляет периметр прямоугольника.

        Возвращает:
        - int: периметр прямоугольника
                """
        return 2 * (self.width + self.height)

    def area(self):
        """
        Вычисляет площадь прямоугольника.

        Возвращает:
        - int: площадь прямоугольника
        """
        return self.width * self.height

    def __add__(self, other):
        """
        Определяет операцию сложения двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - Rectangle: новый прямоугольник, полученный путем сложения двух исходных прямоугольников
        """
        width = self.width + other.width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        """
        Определяет операцию вычитания одного прямоугольника из другого.

        Аргументы:
        - other (Rectangle): вычитаемый прямоугольник

        Возвращает:
        - Rectangle: новый прямоугольник, полученный путем вычитания вычитаемого прямоугольника из исходного
        """
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self.width - other.width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __lt__(self, other):
        """
        Определяет операцию "меньше" для двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - bool: True, если площадь первого прямоугольника меньше площади второго, иначе False
        """
        return self.area() < other.area()

    def __eq__(self, other):
        """
        Определяет операцию "равно" для двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - bool: True, если площади равны, иначе False
        """
        return self.area() == other.area()

    def __le__(self, other):
        """
        Определяет операцию "меньше или равно" для двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - bool: True, если площадь первого прямоугольника меньше или равна площади второго, иначе False
        """
        return self.area() <= other.area()

    def __str__(self):
        """
        Возвращает строковое представление прямоугольника.

        Возвращает:
        - str: строковое представление прямоугольника
        """
        return f"Прямоугольник со сторонами {self.width} и {self.height}"

    def __repr__(self):
        """
        Возвращает строковое представление прямоугольника, которое может быть использовано для создания нового объекта.

        Возвращает:
        - str: строковое представление прямоугольника
        """
        return f"Rectangle({self.width}, {self.height})"

    import sys

    # Открываем файл для записи
    with open('pytest_output.txt', 'w') as file:
        # Перенаправляем stdout в файл
        sys.stdout = file

        # Запускаем pytest.main() с нужными параметрами
        __file__ = None

        doctest.testmod(extraglobs={'__file__': __file__})

    # Возвращаем stdout в исходное состояние
    sys.stdout = sys.__stdout__
    # Считываем содержимое файла
    with open('pytest_output.txt', 'r') as file:
        lines = file.readlines()
        # first_line = file.readline()
        # first_five_lines = lines[:1]

    import re

    file_name = "pytest_output.txt.txt"

    # Открываем файл на чтение
    with open('pytest_output.txt', "r") as file:
        # Считываем содержимое файла
        file_content = file.read()

    # Используем регулярное выражение для удаления "line" и чисел после него
    cleaned_content = re.sub(r'File "__main__", line \d+', '', file_content)

    # Записываем обновленное содержимое обратно в файл
    with open(file_name, "w") as file:
        file.write(cleaned_content)

    with open(file_name, 'r') as new_file:
        file_contents = new_file.read()
        # Выводим содержимое файла на экран
        print(file_contents)

    