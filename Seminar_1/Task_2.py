#Напишите код, который анализирует число num и сообщает, является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым,
# если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
#Если подается отрицательное число или число более 100000, на экран выводится сообщение:
#"Число должно быть больше 1 и меньше 100000."

num = int(input("Введите число: "))

if num <= 1 or num > 100000:
    print("Число должно быть больше 1 и меньше 100000")
else:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    print('Простое' if is_prime else 'Не является простым')

