# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.


def atm():
    balance = 0
    transaction_history = []

    while True:
        print("Доступные действия: пополнить, снять, выйти")
        action = input("Выберите действие: ")

        if action == "пополнить":
            amount = get_amount("Введите сумму для пополнения: ")
            balance += amount
            transaction_history.append(f"Пополнение: +{amount} у.е.")
            apply_interest(balance, transaction_history)
            print(f"Баланс: {balance} у.е.")

        elif action == "снять":
            amount = get_amount("Введите сумму для снятия: ")
            if amount > balance:
                print("Недостаточно средств на счете")
                continue
            fee = calculate_withdrawal_fee(amount)
            total_amount = amount + fee
            balance -= total_amount
            transaction_history.append(f"Снятие: -{total_amount} у.е. (сумма: {amount} у.е., комиссия: {fee} у.е.)")
            apply_interest(balance, transaction_history)
            print(f"Баланс: {balance} у.е.")

        elif action == "выйти":
            print("Завершение программы")
            break

        else:
            print("Недопустимое действие")

        print("-----")

    print("История транзакций:")
    for transaction in transaction_history:
        print(transaction)


def get_amount(prompt):
    while True:
        amount = input(prompt)
        try:
            amount = int(amount)
            if amount % 50 == 0:
                return amount
            else:
                print("Сумма должна быть кратной 50")
        except ValueError:
            print("Некорректная сумма")


def calculate_withdrawal_fee(amount):
    fee = amount * 0.015
    fee = max(fee, 30)
    fee = min(fee, 600)
    return round(fee, 2)


def apply_interest(balance, transaction_history):
    if len(transaction_history) % 3 == 0:
        interest = balance * 0.03
        balance += interest
        transaction_history.append(f"Начисление процентов: +{interest} у.е.")


atm()
