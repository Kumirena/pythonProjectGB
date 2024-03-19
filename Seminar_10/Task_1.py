'''
Создайте базовый класс Animal, который имеет атрибут name, представляющий имя животного.

Создайте классы Bird, Fish и Mammal, которые наследуются от базового класса Animal и добавляют дополнительные атрибуты и методы:

Bird имеет атрибут wingspan (размах крыльев) и метод wing_length, который возвращает длину крыла птицы.

Fish имеет атрибут max_depth (максимальная глубина обитания) и метод depth, который возвращает категорию глубины рыбы (мелководная, средневодная, глубоководная) в зависимости от значения max_depth.
Если максимальная глубина обитания рыбы (max_depth) меньше 10, то она относится к категории "Мелководная рыба".
Если максимальная глубина обитания рыбы больше 100, то она относится к категории "Глубоководная рыба".
В противном случае, рыба относится к категории "Средневодная рыба".

Mammal имеет атрибут weight (вес) и метод category, который возвращает категорию млекопитающего (Малявка, Обычный, Гигант) в зависимости от веса. Если вес объекта меньше 1, то он относится к категории "Малявка".
Если вес объекта больше 200, то он относится к категории "Гигант".
В противном случае, объект относится к категории "Обычный".

Создайте класс-фабрику AnimalFactory, который будет создавать экземпляры животных разных типов на основе переданного типа и параметров. Класс-фабрика должен иметь метод create_animal, который принимает следующие аргументы:

animal_type (строка) - тип животного (один из: 'Bird', 'Fish', 'Mammal').
*args - переменное количество аргументов, представляющих параметры для конкретного типа животного. Количество и типы аргументов могут различаться в зависимости от типа животного.

Метод create_animal должен создавать и возвращать экземпляр животного заданного типа с переданными параметрами.

Если animal_type не соответствует 'Bird', 'Fish' или 'Mammal', функция вызовет ValueError с сообщением 'Недопустимый тип животного'.
'''

class Animal:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def get_info(self) -> str:
        return (f'{"Class:":8}{type(self).__name__}'
                f'\n{"Name:":8}{self.name}'
                f'\n{"Age:":8}{self.age} years')


class Mammal(Animal):

    def __init__(self, name: str, age: int, weight: int, category: str):
        super().__init__(name, age)
        self.weight = weight
        self.category = category



    def get_info(self) -> str:
        return (super().get_info() +
                f'\n{"Weight:":8}{self.weight}'
                f'\n{"Category:":8}{self.category}\n'
                )


class Bird(Animal):

    def __init__(self, name: str, age: int, wingspan: int, wing_length: int):
        super().__init__(name, age)
        self.wingspan = wingspan
        self.wing_length = wing_length



    def get_info(self) -> str:
        return (super().get_info() +
                f'\n{"Wingspan:":8}{self.wingspan}'
                f'\n{"Wing_length:":8}{self.wing_length}\n'
                )


class Fish(Animal):

    def __init__(self, name: str, age: int, max_depth: int, depth: str):
        super().__init__(name, age)
        self.max_depth = max_depth
        self.depth = depth

    def get_info(self) -> str:
        return (super().get_info() +
                f'\n{"Max_depth:":8}{self.max_depth}\n'
                f'\n{"Depth:":8}{self.depth}\n'
                )

