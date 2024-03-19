class NegativeValueError(Exception):
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def __str__(self):
        if self.a <= 0 and self.b <= 0:
            return f"Ошибка ввода: обе стороны имеют невалидные значения = {self.a}; {self.b}"
        else:
            if self.a <= 0:
                return f"Ошибка ввода: сторона имеет невалидное  значение = {self.a} "
            else:
                return f"Ошибка ввода: сторона имеет невалидное  значение  = {self.b}"