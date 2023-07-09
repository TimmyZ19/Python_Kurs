# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

from fractions import Fraction

def calculate_fractions(fraction1, fraction2):
    # Разделение числителя и знаменателя первой дроби
    numerator1, denominator1 = fraction1.split('/')
    numerator1 = int(numerator1)
    denominator1 = int(denominator1)

    # Разделение числителя и знаменателя второй дроби
    numerator2, denominator2 = fraction2.split('/')
    numerator2 = int(numerator2)
    denominator2 = int(denominator2)

    # Создание объектов Fraction
    frac1 = Fraction(numerator1, denominator1)
    frac2 = Fraction(numerator2, denominator2)

    # Вычисление суммы и произведения дробей
    sum_frac = frac1 + frac2
    product_frac = frac1 * frac2

    return sum_frac, product_frac

# Ввод дробей
fraction1 = input("Введите первую дробь в формате a/b: ")
fraction2 = input("Введите вторую дробь в формате a/b: ")

# Вычисление суммы и произведения дробей
sum_frac, product_frac = calculate_fractions(fraction1, fraction2)

# Вывод результатов
print("Сумма дробей:", sum_frac)
print("Произведение дробей:", product_frac)

# Проверка результата с использованием модуля fractions
frac_check = Fraction(fraction1) + Fraction(fraction2)
product_check = Fraction(fraction1) * Fraction(fraction2)
print("Проверка с использованием модуля fractions (сумма):", frac_check)
print("Проверка с использованием модуля fractions (произведение):", product_check)


