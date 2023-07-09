import random
import string

def generate_pseudonyms(num_names, file_name):
    vowels = 'aeiou'
    pseudonyms = []

    while len(pseudonyms) < num_names:
        name_length = random.randint(4, 7)
        name = random.choice(string.ascii_uppercase)  # Начинается с заглавной буквы

        for _ in range(name_length - 1):
            letter = random.choice(string.ascii_lowercase)
            name += letter

        if any(vowel in name for vowel in vowels):  # Обязательно содержит гласные
            pseudonyms.append(name)

    with open(file_name, 'w') as file:
        for pseudonym in pseudonyms:
            file.write(pseudonym + '\n')

# Пример использования
num_names = 10
file_name = "pseudonyms.txt"
generate_pseudonyms(num_names, file_name)
