# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.
# Для генерации случайного числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000

# Генерация случайного числа
num = randint(LOWER_LIMIT, UPPER_LIMIT)

# Цикл для 10 попыток
for attempt in range(1, 11):
    guess = int(input("Попытка №{}: Введите ваше предположение: ".format(attempt)))

    # Проверка угаданного числа
    if guess < num:
        print("Загаданное число больше")
    elif guess > num:
        print("Загаданное число меньше")
    else:
        print("Поздравляю, вы угадали число!")
        break

# Если не угадано за 10 попыток
if guess != num:
    print("Вы исчерпали все попытки. Загаданное число было:", num)
