# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

# date_checker.py

def is_leap_year(year):
    """
    Проверяет, является ли год високосным.
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def check_date(date):
    """
    Проверяет, может ли дата существовать.
    """
    try:
        day, month, year = map(int, date.split('.'))

        # Проверка года
        if year < 1 or year > 9999:
            return False

        # Проверка месяца
        if month < 1 or month > 12:
            return False

        # Проверка дня
        if month == 2:
            if is_leap_year(year):
                max_day = 29
            else:
                max_day = 28
        elif month in [4, 6, 9, 11]:
            max_day = 30
        else:
            max_day = 31

        if day < 1 or day > max_day:
            return False

        return True
    except ValueError:
        return False


if __name__ == '__main__':
    date = input("Введите дату в формате DD.MM.YYYY: ")

    if check_date(date):
        print("Дата может существовать")
    else:
        print("Дата невозможна")
