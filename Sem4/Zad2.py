# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

def process_kwargs(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if not hashable(key):
            key = str(key)
        result[key] = value
    return result

def hashable(obj):
    try:
        hash(obj)
        return True
    except TypeError:
        return False

# Пример
result = process_kwargs(a=10, b="hello", c=[1, 2, 3])
print(result)
