#На вход подается словарь со списком вещей для похода в качестве ключа
# и их массой max_weight в качестве значения.

#Определите какие вещи влезут в рюкзак backpack передав его максимальную грузоподъёмность.
#Предметы не должны дублироваться.

#Результат должен быть в виде словаря {предмет:вес} с вещами в рюкзаке
# и сохранен в переменную backpack.

#Достаточно получить один допустимый вариант и сохранить в переменную backpack.
# Не выводите backpack на экран.

items = {
    "ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1
}
max_weight = 1.0

# вариант комплектации рюкзака по максимально возможной грузоподдьемности
from operator import itemgetter

my_diction = {items}
weight = 0
capacity_backpack = 0
#print("рюкзак: ", my_diction)
#print("список вещей по максимально возможной грузоподьемности рюкзака в ", max_capacity_backpack, "кг")
for things, value in dict(sorted(my_diction.items(), key=itemgetter(1))).items():
    weight += items[things]

    if weight <= max_weight:
        print(things, ' = ', value)
        capacity_backpack += my_diction[things]

print("общий вес рюкзака c вещами: ", capacity_backpack)