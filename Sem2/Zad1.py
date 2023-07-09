# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex используйте для проверки своего результата.

decimal = int(input("Введите целое число: "))

hexadecimal = ""

# Преобразование в шестнадцатеричное представление
while decimal > 0:
    remainder = decimal % 16

    # Преобразование остатка в символ шестнадцатеричной цифры
    if remainder < 10:
        hexadecimal = str(remainder) + hexadecimal
    else:
        hexadecimal = chr(ord('A') + remainder - 10) + hexadecimal

    decimal = decimal // 16

# Проверка результата с использованием встроенной функции hex()
hex_check = hex(int(hexadecimal, 16))

print("Шестнадцатеричное представление числа:", hexadecimal)
print("Проверка с использованием функции hex():", hex_check)
