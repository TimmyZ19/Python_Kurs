# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

def remove_duplicates(lst):
    new_list = []
    for item in lst:
        if item not in new_list:
            new_list.append(item)
    return new_list

# Пример использования
duplicates = [1, 2, 2, 3, 4, 4, 5, 5, 5]
result = remove_duplicates(duplicates)
print(result)
