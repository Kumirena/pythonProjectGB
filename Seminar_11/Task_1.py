import datetime

class MyStr(str):
    """
    My class  comment
    """
    d = 5

    def __new__(cls, value, author_name):
        """
        Создает экземпляр
        :param value:
        :param author_name:
        creation_time = datetime.datetime.now()
        """
        instance = super().__new__(cls, value)
        instance.author_name = author_name
        instance.creation_time = datetime.datetime.now()
        return instance


if __name__ == '__main__':

    s = MyStr("Строка", 'Лев Толстой')            # к этому классу теперь все методы str применимы
    print(s, s.author_name, s.creation_time)
    print(s.upper())
    #print(s.upper().author_name)

    print(MyStr.__doc__)
    print(MyStr.__new__.__doc__)
    print(help(MyStr))